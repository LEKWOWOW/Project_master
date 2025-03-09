class Bus:
    def __init__(self, license_plate, bus_name, capacity):
        self.license_plate = license_plate
        self.bus_name = bus_name
        self.capacity = capacity
        self.available_seat = capacity
        self.seat_list = list(range(1, capacity + 1))

    def book_seat_by_number(self, seat_number):
        if seat_number in self.seat_list:
            self.seat_list.remove(seat_number)
            self.available_seat -= 1
            return True
        return False

    def __str__(self):
        return f"Bus {self.license_plate}, Seats left: {self.available_seat}/{self.capacity}"

class Schedule:
    def __init__(self, schedule_id, route, ticket_price):
        self.schedule_id = schedule_id
        self.route = route
        self.ticket_price = ticket_price
        self.buses = []

    def add_bus(self, bus):
        self.buses.append(bus)

class Ticket:
    def __init__(self, ticket_id, ticket_price):
        self.ticket_id = ticket_id
        self.ticket_price = ticket_price
        self.ticket_status = "Unpaid"

class Payment:
    def __init__(self, payment_id, payment_date, payment_method, ticket):
        self.payment_id = payment_id
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.ticket = ticket

    def process_payment(self):
        self.ticket.ticket_status = "Paid"

class Booking:
    booking_id = 1

    def __init__(self, date, bus, schedule):
        self.booking_id = Booking.booking_id
        self.date = date
        self.status = "Pending"
        self.bus = bus
        self.schedule = schedule
        self.tickets = []
        Booking.booking_id += 1

    def book_seat(self, seat_number):
        if self.bus.book_seat_by_number(seat_number):
            ticket = Ticket(f"T{seat_number}", self.schedule.ticket_price)
            self.tickets.append(ticket)
            return ticket
        return None

class Customer:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.bookings = []
        self.payments = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def make_payment(self, ticket):
        payment = Payment(f"P{ticket.ticket_id}", "01-02-2025", "Cash", ticket)
        payment.process_payment()
        self.payments.append(payment)

class Company:
    def __init__(self):
        self.schedules = []
        self.customers = []
        self.bookings = []

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def add_customer(self, customer):
        self.customers.append(customer)

    def create_booking(self, customer_id, schedule_id, bus_plate, seat_number):
        customer = next((c for c in self.customers if c.user_id == customer_id), None)
        schedule = next((s for s in self.schedules if s.schedule_id == schedule_id), None)
        bus = next((b for b in schedule.buses if b.license_plate == bus_plate), None) if schedule else None

        if customer and schedule and bus:
            booking = Booking("01-02-2025", bus, schedule)
            ticket = booking.book_seat(seat_number)

            if ticket:
                customer.add_booking(booking)
                customer.make_payment(ticket)
                self.bookings.append(booking)
                return f"✅ Seat {seat_number} booked and payment successful! Ticket ID: {ticket.ticket_id}, Price: {ticket.ticket_price} Baht"

        return "❌ Booking failed."
