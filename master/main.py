from fasthtml.common import *
from create_instance import company
from booking import *
from datetime import datetime
app, rt = fast_app()
@rt("/")
def home():
    return Html(
        Head(Title("Bus Booking System")),
        Body(
            H1("Select Schedule 🚌"),
            Ul(
                *[
                    Li(A(f"ตารางเดินรถ: {s.route} (Price: {s.ticket_price} บาท)", 
                         href=f"/schedule/{s.schedule_id}"))
                    for s in company.schedules
                ]
            )
        )
    )
@rt("/schedule/{schedule_id}")
def select_bus(schedule_id: str):
    schedule = next((s for s in company.schedules if s.schedule_id == schedule_id), None)
    
    if not schedule:
        return Html(Body(H2("❌ Schedule not found!"), A("Back", href="/")))

    return Html(
        Body(
            H2(f"Schedule {schedule.route} - Ticket Price: {schedule.ticket_price} Baht"),
            Ul(
                *[
                    Li(A(str(bus), href=f"/bus/{schedule_id}/{bus.license_plate}"))
                    for bus in schedule.buses
                ]
            ),
            A("Back", href="/")
        )
    )
@rt("/bus/{schedule_id}/{license_plate}")
def select_seat(schedule_id: str, license_plate: str):
    schedule = next((s for s in company.schedules if s.schedule_id == schedule_id), None)
    if not schedule:
        return Html(Body(H2("❌ Schedule not found!"), A("Back", href="/")))

    bus = next((b for b in schedule.buses if b.license_plate == license_plate), None)
    if not bus:
        return Html(Body(H2("❌ Bus not found!"), A("Back", href=f"/schedule/{schedule_id}")))

    return Html(
        Body(
            H2(f"Booking seats on {bus.license_plate} - Ticket Price: {schedule.ticket_price} Baht"),
            Form(
                Input(type="number", name="seat_number", placeholder="Seat Number", min=1, max=bus.capacity, required=True),
                Button("Book and Proceed to Payment", type="submit"),
                method="post", action=f"/payment/{schedule_id}/{license_plate}"
            ),
            A("Back", href=f"/schedule/{schedule_id}")
        )
    )
@rt("/payment/{schedule_id}/{license_plate}")
def payment(schedule_id: str, license_plate: str, seat_number: str):
    try:
        seat_number = int(seat_number)
    except ValueError:
        return Html(Body(P("❌ Invalid seat number!"), A("Go Home", href="/")))

    schedule = next((s for s in company.schedules if s.schedule_id == schedule_id), None)
    if not schedule:
        return Html(Body(H2("❌ Schedule not found!"), A("Back", href="/")))

    bus = next((b for b in schedule.buses if b.license_plate == license_plate), None)
    if not bus:
        return Html(Body(H2("❌ Bus not found!"), A("Back", href=f"/schedule/{schedule_id}")))

    # **🔍 ตรวจสอบว่าที่นั่งถูกจองไปแล้วหรือไม่**
    if seat_number not in bus.seat_list:
        return Html(
            Body(
                H2("❌ Payment Failed!"),
                P(f"Seat {seat_number} has already been booked."),
                A("Go Home", href="/")
            )
        )

    booking_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return Html(
        Body(
            H2("Payment Page"),
            P(f"Bus: {license_plate}"),
            P(f"Seat Number: {seat_number}"),
            P(f"Price: {company.schedules[0].ticket_price} Baht"),
            P(f"Booking Time: {booking_time}"),
            Form(
                Input(type="hidden", name="seat_number", value=str(seat_number)),
                Input(type="hidden", name="booking_time", value=booking_time),
                Button("Confirm Payment", type="submit"),
                method="post", action=f"/confirm_payment/{schedule_id}/{license_plate}"
            ),
            A("Cancel", href="/")
        )
    )

@rt("/confirm_payment/{schedule_id}/{license_plate}")
def confirm_payment(schedule_id: str, license_plate: str, seat_number: str):
    try:
        seat_number = int(seat_number)
    except ValueError:
        return Html(Body(P("❌ Invalid seat number!"), A("Go Home", href="/")))

    # ตรวจสอบว่าที่นั่งยังว่างอยู่หรือไม่
    schedule = next((s for s in company.schedules if s.schedule_id == schedule_id), None)
    if not schedule:
        return Html(Body(H2("❌ Schedule not found!"), A("Back", href="/")))

    bus = next((b for b in schedule.buses if b.license_plate == license_plate), None)
    if not bus:
        return Html(Body(H2("❌ Bus not found!"), A("Back", href=f"/schedule/{schedule_id}")))

    if seat_number not in bus.seat_list:
        return Html(
            Body(
                H2("❌ Booking Failed!"),
                P(f"Seat {seat_number} has already been booked."),
                A("Go Home", href="/")
            )
        )

    # ถ้าที่นั่งยังว่าง ให้ทำการจอง
    message = company.create_booking("001", schedule_id, license_plate, seat_number)

    return Html(
        Body(
            H2("✅ Booking Successful!"),
            P(f"Bus: {license_plate}"),
            P(f"Seat Number: {seat_number}"),
            P(f"Price: {company.schedules[0].ticket_price} Baht"),
            P("✅ Payment Confirmed"),
            A("Go Home", href="/")
        )
    )

serve()
