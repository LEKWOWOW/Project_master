from booking import Company, Customer, Schedule, Bus
company = Company()
customer1 = Customer("001", "Bob")
company.add_customer(customer1)
schedule1 = Schedule("S1", "Bangkok - Phuket", 600)
bus1 = Bus("กพ 289 กรุงเทพ", "รถธรรมดา", 10)
schedule1.add_bus(bus1)
company.add_schedule(schedule1)
schedules_data = [
    ("S1", "Bangkok - Phuket", 600),
    ("S2", "Phuket - Bangkok", 786),
    ("S3", "Bangkok - Krabi", 767),
    ("S4", "Krabi - Bangkok", 767),
    ("S5", "Bangkok - Mae Sot", 459),
    ("S6", "Mae Sot - Bangkok", 459),
    ("S7", "Bangkok - Chiang Mai", 651),
    ("S8", "Chiang Mai - Bangkok", 651),
    ("S9", "Bangkok - Sukhothai", 400),
    ("S10", "Sukhothai - Bangkok", 400),
    ("S11", "Bangkok - Phetchabun", 372),
    ("S12", "Phetchabun - Bangkok", 372),
    ("S13", "Bangkok - Trat", 315),
    ("S14", "Trat - Bangkok", 315),
    ("S15", "Bangkok - Chiang Rai", 712),
    ("S16", "Chiang Rai - Bangkok", 712),
    ("S17", "Bangkok - Surat Thani", 611),
    ("S18", "Surat Thani - Bangkok", 611),
    ("S19", "Bangkok - Ranong", 538),
    ("S20", "Ranong - Bangkok", 538),
]

# ✅ กำหนดข้อมูลของรถบัสทั้งหมด
buses_data = [
    ("กพ 289 กรุงเทพ", "รถธรรมดา", 10),
    ("กท 123 กรุงเทพ", "รถวีไอพี", 20),
    ("นค 456 นครราชสีมา", "รถปรับอากาศ", 15),
]

# ✅ วนลูปสร้าง Schedule และเพิ่ม Bus ให้กับแต่ละ Schedule
for schedule_id, route, price in schedules_data:
    schedule = Schedule(schedule_id, route, price)  # ✅ สร้าง Schedule ใหม่
    company.add_schedule(schedule)  # ✅ เพิ่มเข้าไปใน Company
    
    for plate, name, cap in buses_data:
        bus = Bus(plate, name, cap)  # ✅ สร้าง Bus ใหม่
        schedule.add_bus(bus)  # ✅ เพิ่มเข้าไปใน Schedule นั้นๆ

# ✅ ตรวจสอบว่าข้อมูลถูกเพิ่มเรียบร้อย
print(f"📌 Total schedules: {len(company.schedules)}")  
for s in company.schedules:
    print(f"🚌 {s.schedule_id}: {s.route} (Price: {s.ticket_price} Baht, Buses: {len(s.buses)})")
