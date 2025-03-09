class Company:
    def __init__(self, ticket_list, schedule_list, customer_list):
        self.__ticket_list = ticket_list
        self.__schedule_list = schedule_list
        self.__customer_list = customer_list

class Booking:
    booking_id = 1

    def __init__(self, date, status, bus, schedule):
        self.__booking_id = Booking.booking_id
        self.__date = date
        self.__status = status
        self.__bus = bus
        self.__schedule = schedule
        self.__tickets = []
        Booking.booking_id += 1

    def booking_seat_by_number(self, seat_number):
        self.__bus.book_seat_by_number(seat_number)
    
    def add_ticket(self, ticket):
        self.__tickets.append(ticket)

    def book_detail(self):
        return (f"หมายเลขสมุดจอง {self.__booking_id} เวลา {self.__date} สถานะ {self.__status} \n"
                f"Bus: {self.__bus} ตารางเดินรถ {self.__schedule} ตั๋ว: {[t.ticket_detail() for t in self.__tickets]}")

    @property
    def bus(self):
        return self.__bus

class Ticket:
    def __init__(self, ticket_id, ticket_price, ticket_status):
        self.__ticket_id = ticket_id
        self.__ticket_price = ticket_price
        self.__ticket_status = ticket_status

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def ticket_status(self):
        return self.__ticket_status

    @property
    def ticket_price(self):
        return self.__ticket_price

    def ticket_detail(self):
        return f"หมายเลข: {self.__ticket_id}, ราคา: {self.__ticket_price}, สถานะ: {self.__ticket_status}"

class User:
    def __init__(self, user_id, user_name, user_email, user_phone):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_email = user_email
        self.__user_phone = user_phone
        self.__books = []
        self.__payments = []

    def add_booking(self, book):
        if book not in self.__books:
            self.__books.append(book)
            print(f"✔️ เพิ่มสมุดจองแล้ว")
        else:
            print(f"❌ คุณมีสมุดจองหมายเลข {book.booking_id} อยู่แล้ว")

    def add_payment(self, payment):
        self.__payments.append(payment)

    def view_books(self):
        if self.__books:
            for book in self.__books:
                print(book.book_detail())
        else:
            print("❌ ไม่พบสมุดการจองในผู้ใช้นี้")

    def view_payments(self):
        if self.__payments:
            for payment in self.__payments:
                print(payment.payment_detail())
        else:
            print("❌ ไม่พบการจ่ายในผู้ใช้นี้")

class Customer(User): # KONG เราไม่ใช้แล้วออ
    pass

class Payment:
    def __init__(self, payment_id, payment_date, payment_method):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__payment_method = payment_method
        # self.__ticket = [] #KONG 
        self.__ticket = None #KONG มัน error เลยแก้ ถ้าแก้ไปแล้วก็ลบทิ้งได้เลย เพราะตอนนี้ไม่รู้ว่าจะทำแบบไหน

    def payment_detail(self):
        return (f"หมายเลข: {self.__payment_id}, เวลา: {self.__payment_date}, Method: {self.__payment_method}, "
                f"ตั๋ว: {self.__ticket.ticket_id}, ราคา: {self.__ticket.ticket_price}, สถานะ: {self.__ticket.ticket_status}")
    # def add_ticket(self,ticket): #KONG
    #     return self.__ticket.append(ticket) #KONG
    def add_ticket(self,ticket): #KONG มัน error เลยแก้ ถ้าแก้ไปแล้วก็ลบทิ้งได้เลย เพราะตอนนี้ไม่รู้ว่าจะทำแบบไหน
        self.__ticket = ticket #KONG มัน error เลยแก้ ถ้าแก้ไปแล้วก็ลบทิ้งได้เลย เพราะตอนนี้ไม่รู้ว่าจะทำแบบไหน

    def process_payment(self):
        self.__ticket._Ticket__ticket_status = "ชำระเงินเรียบร้อย"
        print(f"✔️ ชำระเงินแล้วเป็นจำนวน {self.__ticket.ticket_price}")

    def process_refund(self):
        self.__ticket._Ticket__ticket_status = "คืนเงินเรียบร้อย"
        print(f"✔️ คืนเงินแล้วเป็นจำนวน {self.__ticket.ticket_price}")

class Bus:
    def __init__(self, license_plate, bus_name, capacity):
        self.__license_plate = license_plate
        self.__bus_name = bus_name
        self.__capacity = capacity
        self.__available_seat = capacity
        self.__seat_list = [i for i in range(1, capacity + 1)]

    @property
    def seat_list(self):
        return self.__seat_list

    def check_available_seat(self):
        return self.__available_seat

    def book_seat_by_number(self, seat_number):
        if seat_number in self.__seat_list:
            self.__seat_list.remove(seat_number)
            self.__available_seat -= 1
            print(f"✔️ จองที่นั่ง {seat_number} สำเร็จ")
        else:
            print(f"❌ ที่นั่ง {seat_number} ไม่ว่าง")

    def __str__(self):
        return f"Bus 🚌 {self.__license_plate} 💺 ที่นั่งคงเหลือ: {self.__available_seat}/{self.__capacity}"

class Schedule:
    def __init__(self, schedule_id, station):
        self.__schedule_id = schedule_id
        self.__station = station
    
    @property
    def schedule_id(self):
        return self.__schedule_id
    
    @property
    def station(self):
        return self.__station

def create_instance():
    bus1 = Bus("กพ 289 กรุงเทพ", "รถธรรมดา", 5)
    print(f"ที่นั่งก่อนจอง: {bus1.seat_list}")

    booking1 = Booking("01-02-2025", "รอดำเนินการ", bus1, "เส้นทาง A")

    booking1.booking_seat_by_number(3)
    booking1.booking_seat_by_number(5)
    booking1.booking_seat_by_number(3)

    print(f"ที่นั่งหลังจอง: {bus1.seat_list}")
    print(bus1)

    ticket1 = Ticket("112", 531, "ยังไม่ได้ชำระเงิน")
    payment1 = Payment("852", "01-02-2025", "cash")
    payment1.add_ticket(ticket1)
    customer = Customer("001", "Bob", "kongza@gmail", "08-2256-1122")
    customer.add_payment(payment1)
    customer.view_payments()
    payment1.process_payment()
    customer.view_payments()

create_instance()

# schedule1(source = "Bankok", destination = "Phuket", price = 786)
# schedule2(source = "Phuket", destination = "Bankok", price = 786)
# schedule3(source = "Bankok", destination = "Krabi", price = 767)
# schedule4(source = "Krabi", destination = "Bankok", price = 767)
# schedule5(source = "Bankok", destination = "Mae Sot", price = 459)
# schedule6(source = "Mae Sot", destination = "Bankok", price = 459)
# schedule7(source = "Bankok", destination = "Chiang Mai", price = 651)
# schedule8(source = "Chiang Mai", destination = "Bankok", price = 651)
# schedule9(source = "Bankok", destination = "Sukhothai", price = 400)
# schedule10(source = "Sukhothai", destination = "Bankok", price = 400)
# schedule11(source = "Bankok", destination = "Phetchabun", price = 372)
# schedule12(source = "Phetchabun", destination = "Bankok", price = 372)
# schedule13(source = "Bankok", destination = "Trat", price = 315)
# schedule14(source = "Trat", destination = "Bankok", price = 315)
# schedule15(source = "Bankok", destination = "Chiang Rai", price = 712)
# schedule16(source = "Chiang Rai", destination = "Bankok", price = 712)
# schedule17(source = "Bankok", destination = "Surat Thani", price = 611)
# schedule18(source = "Surat Thani", destination = "Bankok", price = 611)
# schedule19(source = "Bankok", destination = "Ranong", price = 538)
# schedule20(source = "Ranong", destination = "Bankok", price = 538)