import json
from datetime import datetime
import os 

class Bus:
    def __init__(self, license_plate, bus_name, capacity):
        self.__license_plate = license_plate
        self.__bus_name = bus_name
        self.__capacity = capacity
        self.__available_seat = capacity
        self.__seat_list = list(range(1, capacity + 1))
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @property
    def bus_name(self):
        return self.__bus_name
    
    @property
    def available_seat(self):
        return self.__available_seat
    
    def book_seat_by_number(self, seat_number):
        if seat_number in self.__seat_list:
            self.__seat_list.remove(seat_number)
            self.__available_seat -= 1
            return True
        return False

    def is_available(self):
        return self.__available_seat > 0

class Schedule:
    def __init__(self, schedule_id, route, ticket_price):
        self.__schedule_id = schedule_id
        self.__route = route
        self.__ticket_price = ticket_price
        self.__buses = []
    
    @property
    def schedule_id(self):
        return self.__schedule_id
    
    @property
    def route(self):
        return self.__route
    
    @property
    def ticket_price(self):
        return self.__ticket_price
    
    @property
    def buses(self):
        return self.__buses

    def add_bus(self, bus):
        self.__buses.append(bus)

    def has_available_bus(self):
        return any(bus.is_available() for bus in self.__buses)

class Ticket:
    def __init__(self, ticket_id, ticket_price):
        self.__ticket_id = ticket_id
        self.__ticket_price = ticket_price
        self.__ticket_status = "Unpaid"
    
    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @property
    def ticket_status(self):
        return self.__ticket_status
    
    def mark_paid(self):
        self.__ticket_status = "Paid"

class Payment:
    def __init__(self, payment_id, payment_date, payment_method, ticket):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__payment_method = payment_method
        self.__ticket = ticket

    def process_payment(self):
        self.__ticket.mark_paid()

class Booking:
    booking_id_counter = 1

    def __init__(self, bus, schedule):
        self.__booking_id = Booking.booking_id_counter
        self.__date = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self.__status = "Pending"
        self.__bus = bus
        self.__schedule = schedule
        self.__tickets = []
        Booking.booking_id_counter += 1

    @property
    def booking_id(self):
        return self.__booking_id
    
    def book_seat(self, seat_number):
        if self.__bus.book_seat_by_number(seat_number):
            ticket = Ticket(f"T{seat_number}", self.__schedule.ticket_price)
            self.__tickets.append(ticket)
            return ticket
        return None

class Account:
    user_id_counter = 1

    def __init__(self, user_name, password):
        self.__user_id = f"U{Account.user_id_counter}"
        self.__user_name = user_name
        self.__password = password
        self.__bookings = []
        self.__payments = []
        Account.user_id_counter += 1

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def bookings(self):
        return self.__bookings

class Customer(Account):
    pass

class Company:
    def __init__(self):
        self.__schedules = []
        self.__customers = []
        self.__bookings = []
        self.load_data()
    
    @property
    def schedules(self):
        return self.__schedules
    
    def add_schedule(self, schedule):
        self.__schedules.append(schedule)
        self.save_data()

    def add_customer(self, user_name, password):
        new_customer = Customer(user_name, password)
        self.__customers.append(new_customer)
        self.save_data()  
        
        return new_customer.user_id

    def authenticate(self, user_id, password):
        self.load_data()
        return next((c for c in self.__customers if c.user_id == user_id and c._Account__password == password), None)

    def is_schedule_available(self, schedule_id):
        schedule = next((s for s in self.__schedules if s.schedule_id == schedule_id), None)
        return schedule.has_available_bus() if schedule else False

    def create_booking(self, customer_id, schedule_id, bus_plate, seat_number):
        customer = next((c for c in self.__customers if c.user_id == customer_id), None)
        schedule = next((s for s in self.__schedules if s.schedule_id == schedule_id), None)
        bus = next((b for b in schedule.buses if b.license_plate == bus_plate), None) if schedule else None
        if customer and schedule and bus:
            booking = Booking(bus, schedule)
            ticket = booking.book_seat(seat_number)
            if ticket:
                customer.bookings.append(booking)
                self.__bookings.append(booking)
                self.save_data()
                return f"✅ Seat {seat_number} booked successfully!"
        return "❌ Booking failed."

    def save_data(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            json_file_path = os.path.join(current_dir, "company_data.json")

            data = {
                "customers": [
                    {"user_id": c.user_id, "user_name": c.user_name, "password": c._Account__password}
                    for c in self.__customers
                ],
                "schedules": [
                    {
                        "schedule_id": s.schedule_id,
                        "route": s.route,
                        "ticket_price": s.ticket_price,
                        "buses": [
                            {"license_plate": b.license_plate, "bus_name": b.bus_name, "capacity": b.available_seat}
                            for b in s.buses
                        ],
                    }
                    for s in self.__schedules
                ],
            }

            with open(json_file_path, "w") as file:
                json.dump(data, file, indent=4)

            print(f"✅ Data saved successfully at: {json_file_path}")
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    def load_data(self):
        try:
             with open("company_data.json", "r") as file:
                data = json.load(file)
                self.__customers = [
                    Customer(c["user_name"], c["password"]) for c in data.get("customers", [])
                ]
                self.__schedules = [
                    Schedule(s["schedule_id"], s["route"], s["ticket_price"]) for s in data.get("schedules", [])
                ]
        except FileNotFoundError:
            print("No existing data found. Starting fresh.")
