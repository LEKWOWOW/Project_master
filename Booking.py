class Compny:
    def __init__(self,ticket_list,schedule_list,customer_list):
        self.__ticket_list = ticket_list
        self.__schedule_list = schedule_list

class Booking:
    booking_id = 1
    def __init__(self,date,status,bus,schedule):
        self.__booking_id = Booking.booking_id
        self.__date = date
        self.__status = status
        self.__bus = bus
        self.__schedule = schedule
        self.__tickets = []
        Booking.booking_id +=1
    def booking_seat(self,seat_book):
        if  self.__bus.check_available_seat() >= seat_book:
            self.__bus.reuce_seat(seat_book)
            self.__status ="✔️จองสำเร็จ"
        else:
            print("❌ไม่มีที่เหลือแล้วจ้า")
    def add_ticket(self,ticket):
        self.__tickets.append(ticket)
    def book_detail(self):
        return (f"หมายเลขสมุดจอง{self.__booking_id} เวลา{self.__date} สถานะ{self.__status} bus {self.__bus} ตารางเดินรถ {self.__schedule} ตั๋ว{self.__tickets}")
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
        else: print(f"❌ คุณมีสมุดจองหมายเลข {book.booking_id} อยู่แล้ว")
    def add_payment(self, payment):
        self.__payments.append(payment)
    def view_books(self):
        if self.__books:
            for number, book in enumerate(self.__books, 1):
                print(f"{number}. {book.book_detail()}")
        else: print(f"❌ ไม่พบสมุดการจองในผู้ใช้นี้")
    def view_payments(self):
        if self.__payments:
            for number, payment in enumerate(self.__payments, 1):
                print(f"{number}. {payment.payment_detail()}")
        else: print(f"❌ ไม่พบการจ่ายในผู้ใช้นี้")
    def payment_by_ticket_id(self, ticket_id):
        if self.__books:
            for book in self.__books:
                for ticket in book.tickets.ticket_id:
                    if ticket.ticket_id == ticket_id:
                        if ticket.ticket_status == "ยังไม่ได้ชำระเงิน":
                            ticket.process_payment(ticket.ticket_price)
                            return
                        else:
                            print(f"❌ ไม่สามารถชำระเงินได้")
            print(f"❌ ไม่พบตั๋ว")
        else: print(f"❌ ไม่พบสมุดการจองในผู้ใช้นี้")
    def refund_by_ticket_id(self, ticket_id):
        if self.__books:
            for book in self.__books:
                for ticket in book.tickets.ticket_id:
                    if ticket.ticket_id == ticket_id:
                        if ticket.ticket_status == "ชำระเงินเรียบร้อย":
                            ticket.process_refund(ticket.ticket_price)
                            return
                        else:
                            print(f"❌ ไม่สามารถคืนเงินได้")
            print(f"❌ ไม่พบตั๋ว")
        else: print(f"❌ ไม่พบสมุดการจองในผู้ใช้นี้")

class Customer(User):
    def __init__(self, user_id, user_name, user_email, user_phone):
        super().__init__(user_id, user_name, user_email, user_phone)
    def add_booking(self, book):
        return super().add_booking(book)
    def add_payment(self, payment):
        return super().add_payment(payment)
    def view_books(self):
        return super().view_books()
    def view_payments(self):
        return super().view_payments()
    
class Payment:
    def __init__(self, payment_id, payment_date, payment_method, ticket = Ticket):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__payment_method = payment_method
        self.__ticket = ticket
    def payment_detail(self):
        return f"หมายเลข: {self.__payment_id}, เวลา: {self.__payment_date}, Method: {self.__payment_method}, ตั๋ว: {self.__ticket.ticket_id}, ราคา: {self.__ticket.ticket_price}, สถานะ: {self.__ticket.ticket_status}"
    def process_payment(self, price):
        self.__ticket.ticket_status = "ชำระเงินเรียบร้อย"
        print(f"ชำระเงินแล้วเป็นจำนวน {price}")
    def process_refund(self, price):
        self.__ticket.ticket_status = "คืนเงินเรียบร้อย"
        print(f"คืนเงินแล้วเป็นจำนวน {price}")
    
class Station:
    def __init__(self,station_id,station_name,capacity):
        self.__station_id = station_id
        self.__station_name = station_name
    def __str__(self):
        pass
      

    @property
    def station_id(self):
        return self.__station_id
    @property
    def station_name(self):
        return self.__station_name
class Seat:
    def __init__(self,seat_id):
        self.__seat_id
    
class Bus:
    def __init__(self,license_plate,bus_name,capacity):
        self.__license_plate = license_plate
        self.__bus_name = bus_name
        self.__capacity = capacity
        self.__available_seat = capacity
    @property
    def license_plat(self):
        return self.__bus_id
    def check_available_seat(self):
        return self.__available_seat 
    def reuce_seat(self,number_seat):
        if number_seat <= self.__available_seat:
             self.__available_seat -= number_seat
        else:
            print("❌ ไม่มีที่ว่างเหลือละจะ ")
    def __str__(self):
        return f"Bus 🚌 {self.__license_plate} 💺 ที่นั่งคงเหลือ: {self.__available_seat}/{self.__capacity}"
class Schedule:
    def __init__(self,schedule_id):
        self.__schedule_id =schedule_id
        self.__station_number = Station.station_id
        self.__station_name = Station.station_name
    @property
    def schedule_id(self):
        return self.__schedule_id
    @property
    def station_name(self):
        return self.__station_name
    @property
    def station_number(self):
        return self.__station_number
def create_instance():
     bus_list = []
     bus1 = Bus("กพ 289 กรุงเทพ","รถธรรมดา",20)
     bus2 = Bus("กพ 309 เพชรบุรี","รถปรับอากาศ",20)
     bus3 = Bus("กช 208 ลำปาง","รถเอกชนร่วมบริการปรับอากาศ",25)
     user  = User("001", "bob", "kongza@gmail", "08-2256-1122")
     man1 = Customer("001", "bob", "kongza@gmail", "08-2256-1122")
     ticket1 = Ticket("112", 531, "ยังไม่ได้ชำระเงิน") ## ราคาเดวคำนวณจาก สถานี ต้นทาง ดีไหมนะ แต่ไม่รู้ไงว่าหน่วยละเท่าไรหรือเอา เป็นราคาที่ฟิกไปเลย คือไม่รู้ว่า เราวิ่งผ่านหนึ่งสถานี มันจะเสียเท่าไหร่อะดิ ช่วยคิดหน่อย
     bus_list.append(bus1)
     bus_list.append(bus2)
     bus_list.append(bus3)
     print(ticket1.ticket_detail())
     payment1 = Payment("852", "01-02-2003", "cash", ticket1)
     man1.add_payment(payment1)
     man1.view_payments()
create_instance()
     
######เดวว่ากันต่อ#####



    
        