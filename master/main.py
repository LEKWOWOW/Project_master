from fasthtml.common import *
from create_instance import company
from booking import *

app, rt = fast_app()

@rt("/")
def home():
    return Html(
        Head(Title("Bus Booking System")),
        Body(
            H1("Select Schedule 🚌"),
            Ul(
                *[Li(A(f"Schedule: {s.route} (Price: {s.ticket_price} Baht)", href=f"/schedule/{s.schedule_id}")) for s in company.schedules]
            )
        )
    )

@rt("/schedule/{schedule_id}")
def select_bus(schedule_id: str):
    schedule = next(s for s in company.schedules if s.schedule_id == schedule_id)
    return Html(
        Body(
            H2(f"Schedule {schedule.route} - Ticket Price: {schedule.ticket_price} Baht"),
            Ul(
                *[Li(A(str(bus), href=f"/bus/{schedule_id}/{bus.license_plate}")) for bus in schedule.buses]
            ),
            A("Back", href="/")
        )
    )

@rt("/bus/{schedule_id}/{license_plate}")
def select_seat(schedule_id: str, license_plate: str):
    schedule = next(s for s in company.schedules if s.schedule_id == schedule_id)
    return Html(
        Body(
            H2(f"Booking seats on {license_plate} - Ticket Price: {schedule.ticket_price} Baht"),
            Form(
                Input(type="number", name="seat_number", placeholder="Seat Number", min=1, max=10, required=True),
                Button("Book and Pay", type="submit"),
                method="post", action=f"/book_and_pay/{schedule_id}/{license_plate}"
            ),
            A("Back", href=f"/schedule/{schedule_id}")
        )
    )

@rt("/book_and_pay/{schedule_id}/{license_plate}")
def book_and_pay(schedule_id: str, license_plate: str, seat_number: int):
    message = company.create_booking("001", schedule_id, license_plate, seat_number)
    return Html(
        Body(
            P(message),
            A("Go Home", href="/")
        )
    )

serve()
