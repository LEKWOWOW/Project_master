from fasthtml.common import *
from create_instance import company

app, rt = fast_app()

@rt("/")
def home():
    """แสดงตารางเดินรถทั้งหมด"""
    return Html(
        Head(Title("Bus Booking System")),
        Body(
            H1("Select Schedule 🚌"),
            Ul(
                *[
                    Li(
                        A(f"ตารางเดินรถ: {s.route} (Price: {s.ticket_price} บาท)", href=f"/schedule/{s.schedule_id}"),
                        " ✅ มีที่นั่งว่าง" if company.is_schedule_available(s.schedule_id) else " ❌ เต็มแล้ว"
                    )
                    for s in company.schedules
                ]
            )
        )
    )

@rt("/schedule/{schedule_id}")
def select_bus(schedule_id: str):
    """เลือก Bus สำหรับตารางเดินรถที่เลือก"""
    if not company.is_schedule_available(schedule_id):
        return Html(Body(H2("❌ Schedule is fully booked!"), A("Back", href="/")))

    schedule = next((s for s in company.schedules if s.schedule_id == schedule_id), None)

    return Html(
        Body(
            H2(f"Schedule {schedule.route} - Ticket Price: {schedule.ticket_price} Baht"),
            Ul(
                *[
                    Li(A(str(bus), href=f"/bus/{schedule_id}/{bus.license_plate}"))
                    for bus in schedule.buses if bus.available_seat > 0  
                ]
            ),
            A("Back", href="/")
        )
    )

@rt("/bus/{schedule_id}/{license_plate}")
def select_seat(schedule_id: str, license_plate: str):
    """เลือกที่นั่งบน Bus"""
    return Html(
        Body(
            H2(f"Booking seats for Bus {license_plate}"),
            Form(
                Input(type="number", name="seat_number", placeholder="Seat Number", min=1, required=True),
                Button("Book and Pay", type="submit"),
                method="post", action=f"/book_and_pay/{schedule_id}/{license_plate}"
            ),
            A("Back", href=f"/schedule/{schedule_id}")
        )
    )

@rt("/book_and_pay/{schedule_id}/{license_plate}")
def book_and_pay(schedule_id: str, license_plate: str, seat_number: str):
    """ทำการจองที่นั่งและจ่ายเงิน"""
    try:
        seat_number = int(seat_number)
    except ValueError:
        return Html(Body(P("❌ Invalid seat number!"), A("Go Home", href="/")))

    message = company.create_booking("001", schedule_id, license_plate, seat_number)

    return Html(
        Body(
            P(message),
            A("Go Home", href="/")
        )
    )

serve()
