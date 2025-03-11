import json
from datetime import datetime
import os

class Bus:
    def __init__(self, license_plate, bus_name, capacity):
        self.__license_plate = license_plate
        self.__bus_name = bus_name
        self.__capacity = capacity
        self.__available_seat = capacity
        self.__seat_list = list(range(1, capacity + 1))  # ที่นั่งเริ่มต้น 1 ถึง capacity

    @property
    def license_plate(self):
        return self.__license_plate

    @property
    def bus_name(self):
        return self.__bus_name

    @property
    def available_seat(self):
        return self.__available_seat

    @property
    def seat_list(self):
        return self.__seat_list

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

class Account:
    user_id_counter = 1

    def __init__(self, user_id, user_name, password):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__password = password
        self.__bookings = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def bookings(self):
        return self.__bookings

class Customer(Account):
    def __init__(self, user_name, password):
        user_id = f"U{Account.user_id_counter}"
        super().__init__(user_id, user_name, password)
        Account.user_id_counter += 1

class Company:
    def __init__(self):
        self.__schedules = []
        self.__customers = []
        self.__bookings = []
        self._load_data()

    @property
    def schedules(self):
        return self.__schedules

    def get_bus(self, schedule_id, bus_plate):
        schedule = next((s for s in self.__schedules if s.schedule_id == schedule_id), None)
        if not schedule:
            return None
        return next((b for b in schedule.buses if b.license_plate == bus_plate), None)

    def add_schedule(self, schedule):
        existing_schedule = next((s for s in self.__schedules if s.schedule_id == schedule.schedule_id), None)
        if not existing_schedule:
            self.__schedules.append(schedule)
            self._save_data()

    def add_bus_to_schedule(self, schedule_id, license_plate, bus_name, capacity):
        schedule = self.schedule_select(schedule_id)
        if schedule:
            bus = Bus(license_plate, bus_name, capacity)
            schedule.add_bus(bus)
            self._save_data()

    def book_seat(self, customer_id, schedule_id, bus_plate, seat_number):
        customer = next((c for c in self.__customers if c.user_id == customer_id), None)
        bus = self.get_bus(schedule_id, bus_plate)

        if not customer or not bus:
            return "❌ จองไม่ได้นะเอ้อ"

        if bus.book_seat_by_number(seat_number):
            customer.bookings.append(f"Booking: {bus.bus_name}, Seat: {seat_number}")
            self._save_data()
            return f"✅ Seat {seat_number} booked successfully for {bus.bus_name}!"
        else:
            return "❌ ที่นั่งนี้ถูกจองไปแล้ว"

    def get_customer_by_name(self, user_name):
        return next((c for c in self.__customers if c.user_name == user_name), None)

    def authenticate(self, user_name, password):
        return next((c for c in self.__customers if c.user_name == user_name and c.password == password), None)

    def add_customer(self, user_name, password):
        if self.get_customer_by_name(user_name):
            return None  
        new_customer = Customer(user_name, password)
        self.__customers.append(new_customer)
        self._save_data()
        return new_customer.user_id

    def schedule_select(self, schedule_id):
        return next((b for b in self.__schedules if b.schedule_id == schedule_id), None)

    def _save_data(self):
        data = {
            "customers": [
                {"user_id": c.user_id, "user_name": c.user_name, "password": c.password}
                for c in self.__customers
            ],
            "schedules": [
                {
                    "schedule_id": s.schedule_id,
                    "route": s.route,
                    "ticket_price": s.ticket_price,
                    "buses": [
                        {
                            "license_plate": b.license_plate,
                            "bus_name": b.bus_name,
                            "capacity": b._Bus__capacity,
                            "available_seat": b.available_seat,
                            "seat_list": b.seat_list
                        }
                        for b in s.buses
                    ],
                }
                for s in self.__schedules
            ],
            "user_id_counter": Account.user_id_counter
        }
        with open("company_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def _load_data(self):
        try:
            with open("company_data.json", "r") as file:
                data = json.load(file)
                Account.user_id_counter = data.get("user_id_counter", 1)

                for user in data.get("customers", []):
                    customer = Customer(user["user_name"], user["password"])
                    customer._Account__user_id = user["user_id"]
                    self.__customers.append(customer)

                for sched in data.get("schedules", []):
                    schedule = Schedule(sched["schedule_id"], sched["route"], sched["ticket_price"])
                    for bus in sched.get("buses", []):
                        bus_instance = Bus(bus["license_plate"], bus["bus_name"], bus["capacity"])
                        bus_instance._Bus__available_seat = bus.get("available_seat", bus["capacity"])
                        bus_instance._Bus__seat_list = bus.get("seat_list", list(range(1, bus["capacity"] + 1)))
                        schedule.add_bus(bus_instance)

                    self.add_schedule(schedule)
        except FileNotFoundError:
            pass
