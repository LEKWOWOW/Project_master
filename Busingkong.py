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
        self.__tickets = []     #KONG
        Booking.booking_id +=1
    @property
    def bus(self):
        return self.__bus
    @property
    def booking_id(self): # KONG
        return self.__booking_id
    @property
    def tickets(self): # KONG
        return self.__tickets
    def booking_seat(self,seat_book):
        if  self.__bus.check_available_seat() >= seat_book:
            self.__bus.reuce_seat(seat_book)
            self.__status ="✔️ จองสำเร็จ"
        else:
            print("❌ ไม่มีที่เหลือแล้วจ้า")
    def add_ticket(self, ticket): # KONG
        if ticket not in self.__tickets:
            self.__tickets.append(ticket)
            print(f"✔️ เพิ่มตั๋วเรียบร้อย")
        else: print(f"❌ ตั๋วหมายเลข {ticket.ticket_id} มีอยู้ในเลขสมุดการการจอง {self.__booking_id} แล้ว")
    def check_in(self, ticket_id): # KONG
        if self.__status:
            for ticket in self.__tickets:
                if ticket.ticket_id == ticket_id:
                    if ticket.ticket_status == "ชำระเงินเรียบร้อย":
                        ticket.ticket_status = "เช็คอินแล้ว"
                        print(f"✔️ ตั๋ว {ticket.ticket_id} {ticket.ticket_status}")
                        return
                    else:
                        print(f"❌ ตั๋ว {ticket.ticket_id} ยังไม่ได้ชำระเงิน")
                        return
            print(f"❌ ไม่พบตั๋ว {ticket_id} ในเลขสมุดการการจอง {self.__booking_id}")
        else: print(f"❌ ไม่พบตั๋วในสมุดการจองหมายเลข {self.__booking_id}")
    def book_detail(self): # KONG
        info = f"หมายเลข: {self.__booking_id}, เวลา: {self.__date}, สถานะ: {self.__status}, Bus: {self.__bus}, ตารางเวลา: {self.__schedule}"
        if self.__tickets:
            detail_str = ", ".join([ticket.ticket_id for ticket in enumerate(self.__tickets, 1)])
            info += f"ตั๋ว: {detail_str}"
        else: info += "ไม่พบตั๋วในสมุดการจองนี้"
        return info
    def view_tickets(self): # KONG
        if self.__tickets:
            for number, ticket in enumerate(self.__tickets, 1):
                print(f"{number}. {ticket.ticket_detail()}")
        else: print(f"❌ ไม่พบตั๋วในสมุดการจองหมายเลข {self.__booking_id}") 
    def cancel_booking(self): #KONG ถ้าจะทำเราต้องมี owner
        # if owner = owner 
        # status = "cancel" 
        pass
    
class Station:
    def __init__(self,station_id,station_name,capacity):
        self.__station_id = station_id
        self.__station_name = station_name
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
        self.__schedule_id = schedule_id
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
    
############################################### KONG

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
    
def create_instance():
    bus_list = []
    bus1 = Bus("กพ 289 กรุงเทพ","รถธรรมดา",20)
    bus2 = Bus("กพ 309 เพชรบุรี","รถปรับอากาศ",20)
    bus3 = Bus("กช 208 ลำปาง","รถเอกชนร่วมบริการปรับอากาศ",25)
    bus_list.append(bus1)
    bus_list.append(bus2)
    bus_list.append(bus3)
    # print(bus_list)
    ######################################### KONG
    man1 = Customer("001", "bob", "kongza@gmail", "08-2256-1122")
    ticket1 = Ticket("112", 531, "ยังไม่ได้ชำระเงิน") # price อันนี้เราต้องไปดึงมาชะ ดึงจาก sation ไปเก็บไว้ในticket เราจะคำนว๊จาก stationดีไหมเงินอะ
    #man1_book = Booking("03-08-2546", "เปิดใช้งาน", bus1, None) #class Booking ใช้ไงงง
    print(ticket1.ticket_detail())
    # man1.add_booking(man1_book)
    # man1.view_books()
    # man1_book.add_ticket(ticket1)
    # man1.view_books()
    payment1 = Payment("852", "01-02-2003", "cash", ticket1)
    man1.add_payment(payment1)
    man1.view_payments()
    # man1.payment_by_ticket_id("112")
    # man1.refund_by_ticket_id("112")
    # man1.view_payments()
create_instance()