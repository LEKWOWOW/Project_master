from booking import Company, Customer, Schedule, Bus

# สร้าง instance ของบริษัท
company = Company()

# เพิ่มลูกค้า
customer1 = Customer("001", "Bob")
company.add_customer(customer1)

# สร้างตารางเวลาและเพิ่มรถบัส
schedule1 = Schedule("S01", "Route A", 600)
bus1 = Bus("กพ 289 กรุงเทพ", "รถธรรมดา", 10)
schedule1.add_bus(bus1)

# เพิ่มตารางเวลาเข้าในบริษัท
company.add_schedule(schedule1)
