class Compny:
    def __init__(self,ticket_list,schedule_list,customer_list):
        self.__ticket_list = ticket_list
        self.__schedule_list = schedule_list
        self.__customer_list = customer_list
class Booking:
    def __init__(self,booking_id,date,status):
        self.__booking_id = booking_id
        self.__date = date
        self.__statu = status
class Station:
    def __init__(self,station_id,station_name):
        self.__station_id = station_id
        self.__station_name = station_name
    @property
    def station_id(self):
        return self.__station_id
    @property
    def station_name(self):
        return self.__station_name
class Schedule:
    def __init__(self,schedule_id):
        self.__schedule_id =schedule_id
        self.__station_number = Station.station_id
        self.__station_name = Station.station_name
    @property
    def schedule_id(self):
        return self.__schedule_id
    @property
    def station_number(self):
        return self.__station_number
station1 = Station("10","gg")
schedule1 = Schedule(10)
print(schedule1.station_number)
    
        