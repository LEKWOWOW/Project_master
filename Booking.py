class Compny:
    def __init__(self,ticket_list,schedule_list,customer_list):
        self.__ticket_list = ticket_list
        self.__schedule_list = schedule_list
class Booking:
    booking_id = 1
    def __init__(self,date,status,bus):
        self.__booking_id = Booking.booking_id
        self.__date = date
        self.__status = status
        self.__bus = bus
        Booking.booking_id +=1
    def booking_seat(self,seat_book):
        if  self.__bus.check_available_seat() >= seat_book:
            self.__bus.reuce_seat(seat_book)
            self.__status ="✔️จองสำเร็จ"
        else:
            print("❌ไม่มีที่เหลือแล้วจ้า")
        
    def show_all(self):
        print(f"")
    def add_bus(self,bus):
        self.__bus.append(bus)
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
    def __init__(self,bus_id,bus_name,capacity):
        self.__bus_id = bus_id
        self.__bus_name = bus_name
        self.__capacity = capacity
        self.__available_seat = capacity
    def check_available_seat(self):
        return self.__available_seat 
    def reuce_seat(self,number_seat):
        if number_seat <= self.__available_seat:
             self.__available_seat -= number_seat
        else:
            print("❌ ไม่มีที่ว่างเหลือละจะ ")
    def __str__(self):
        return f"Bus {self.__bus_name} | ที่นั่งคงเหลือ: {self.__available_seat}/{self.__capacity}"
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
     bus1 = Bus("B301","รถมินิบัส",40)
     booking = Booking("02-9-2025","OK",bus1)
     booking.booking_seat(20)
     print(bus1)
create_instance()


    
        