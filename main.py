import json
from datetime import datetime
import os
from fasthtml.common import *
from create_instance import company
from fastapi.staticfiles import StaticFiles

app, rt = fast_app()

app.mount("/static", StaticFiles(directory="./static"), name="style.css")
app.mount("/static", StaticFiles(directory="./static"), name="specai_page.css")
app.mount("/static", StaticFiles(directory="./static"), name="schedule.css")
app.mount("/static", StaticFiles(directory="./static"), name="pop.css")
app.mount("/static", StaticFiles(directory="./static"), name="login.css")
app.mount("/static", StaticFiles(directory="./static"), name="schedule.css")
app.mount("/static", StaticFiles(directory="./static"), name="select_bus.css")
app.mount("/static", StaticFiles(directory="./static"), name="select_seat.css")
app.mount("/static", StaticFiles(directory="./static"), name="ิbooking_status.css")
app.mount("/static", StaticFiles(directory="./static"), name="payment_success.css")
app.mount("/static", StaticFiles(directory="./static"), name="refund_success")
session = {}

@rt("/")
def home():
    user_name = session.get("user_name")
    if not user_name:
        return Html(
            Head(
                Link(rel="stylesheet", href="/static/style.css")
            ),
            Body(
                Header(
                    H4("Good_job", _class="logo"),
                    Nav(
                        A("Register", _class="menu-item", href="/register"),
                        A("Login", _class="menu-item", href="/login"),
                         A("Logout", _class="menu-item", href="/logout"),
                        A("Home", _class="menu-item ", href="/bus_schedule"),
                        A("ดูตั๋ว", _class="menu-item ", href="/view_tickets"),
                    )
                ),
                Div(
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    _class="container",
                ),
                Div(
                    H1("บริษัท", Span("ขนส่ง", _class="pink"), " บขส"),
                    _class="layer",
                ),
                Footer(
                    P("บขสร้ายๆ ", A("กลับหน้าหลัก", href="/", _class="link"), ". 24/3"),
                    Div("", _class="")
                )
            ), _class="home-page"
        )
    return Html(
            Head(
                Link(rel="stylesheet", href="/static/style.css")
            ),
            Body(
                Header(
                    H4("Good_job", _class="logo"),
                    Nav(
                        A("Register", _class="menu-item", href="/register"),
                        A("Login", _class="menu-item", href="/login"),
                         A("Logout", _class="menu-item", href="/logout"),
                        A("Home", _class="menu-item ", href="/bus_schedule"),
                        A("ดูตั๋ว", _class="menu-item ", href="/view_tickets"),
                    )
                ),
                Div(
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    Div(Div(_class="front"), Div(_class="back"), _class="panel"),
                    _class="container",
                ),
                Div(
                    H1("บริษัท", Span("ขนส่ง", _class="pink"), " บขส"),
                    _class="layer",
                ),
                Footer(
                    P("บขสร้ายๆ ", A("กลับหน้าหลัก", href="/", _class="link"), ". 24/3"),
                    Div("", _class="")
                )
            ), _class="home-page"
        )
   

@rt("/user_profile")
def user_profile():
    user_name = session.get("user_name")
    
    if not user_name:
        return Redirect("/login")
    
    user_data = company.get_customer_by_name(user_name)

    return Html(
        Head(
            Link(rel="stylesheet", href="/static/user_profile.css")
        ),
        Body(
            Div(
                H1(user_data.user_id, _class="user-name"),
                P("📧 " + user_data.user_name, _class="user-email"),
                P("👤 Username: " + user_data.password , _class="user-username"),
                Div(
                    Button("🚪 ออกจากระบบ", _class="logout-btn", onclick="window.location.href='/logout'"),
                    _class="button-group"
                ),
                Div(
                    Button("📅 SCHEDULE", _class="logout-btn", 
                        onclick=f"window.location.href='/bus_schedule?user_name={user_name}'"),
                    _class="button-group"
                ),
                _class="profile-container"
            )
        )
    )

# @rt("/select_bus")
# def select_bus(schedule_id: str = None):
#     schedule = company.schedule_select(schedule_id)
#     if not schedule:
#         return 
@rt("/show_invalid")
def show_invalid():
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/invalid.css")
        ),
        Body(
            Div(
                H1("❌ INVALID ❌", _class="invalid-title"),
                P("ขออภัย! คุณไม่มีสิทธิ์เข้าถึงหน้านี้", _class="invalid-text"),
                Button("กลับไปหน้าหลัก", _class="invalid-btn", onclick="window.location.href='/'"),
                _class="invalid-container"
            )
        )
    )
@rt("/show_P")
def show_invalid():
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/invalid.css")
        ),
        Body(
            Div(
                H1("❌ มีคนใช้ชื่อนี้ไปแล้ว ❌", _class="invalid-title"),
                P("กรุณาใช้ชื่ออื่น", _class="invalid-text"),
                Button("กลับไปหน้าหลัก", _class="invalid-btn", onclick="window.location.href='/'"),
                _class="invalid-container"
            )
        )
    )
@rt("/show_l")
def show_invalid():
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/invalid.css")
        ),
        Body(
            Div(
                H1("❌ ไม่พบชื่อผู้ใช้นี้ ❌", _class="invalid-title"),
                P(" ไม่พบชื่อผู้ใช้นี้", _class="invalid-text"),
                Button("กลับไปหน้าหลัก", _class="invalid-btn", onclick="window.location.href='/'"),
                _class="invalid-container"
            )
        )
    )

    #        Body(
    #         Div(
    #             Div(
    #                 Div(
    #                     P("1", _class="date"),
    #                     P("2", _class="date"),
    #                     P("3", _class="date"),
    #                     P("4", _class="date"),
    #                     P("5", _class="date"),
    #                     P("6", _class="date"),
    #                     P("7", _class="date"),
    #                     P("8", _class="date"),
    #                     P("9", _class="date"),
    #                     P("10", _class="date"),
    #                     _class="special-item"
    # )
    # )
    #         )
    #        )
    # )
# @rt("/special")
# def special():
#     return Html(
#         Head(
#             Link(rel="stylesheet", href="/static/specai_page.css")
#         ),
#         Body(
#             Div(
#                 Div(
#                     Div(
#                         P("1", _class="date"),
#                         P("2", _class="date"),
#                         P("3", _class="date"),
#                         P("4", _class="date"),
#                         P("5", _class="date"),
#                         P("6", _class="date"),
#                         P("7", _class="date"),
#                         P("8", _class="date"),
#                         P("9", _class="date"),
#                         P("10", _class="date"),
#                         _class="special-item"
#                     ),
#                     _class="special-container"
#                 ),
#                 _class="special-page",
#             )
#         )
#     )
# @rt("/schedule_list")
@rt("/register")
def register():
    
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/style.css")
        ),
        Body(
            Div(
                Form(
                    H1("Register", _class="title"),
                    Div(
                        Input(type="text", name="user_name", placeholder="", required=True, _class="input"),
                        Div(_class="cut"),
                        Label("User Name", _class="placeholder", _for="User Name"),
                        _class="input-container ic1"
                    ),
                    Div(
                        Input(type="password", name="password", placeholder="", required=True, _class="input"),
                        Div(_class="cut cut-short"),
                        Label("Password", _class="placeholder", _for="Password"),
                        _class="input-container ic2"
                    ),
                    Div(  
                        Button("Register", type="submit", _class="submit"),
                        Button("Home", type="button", _class="submit home-btn", onclick="window.location.href='/'"),
                        _class="button-group"
                    ),
                    method="post", action="/process_register",
                    _class="form-box",
                )
            )
        )
    )
@rt("/process_register")
def process_register(user_name: str = None, password: str = None):
    print(f"📌 Register request received: user_name={user_name}, password={password}")
    if not user_name or not password:
        print(f"📌 Register request received: user_name={user_name}, password={password}")
        return Redirect ("/show_P")
    
    existing_user = company.get_customer_by_name(user_name)
    if existing_user:
        return Redirect ("/show_P")
    
    session["user_name"] = user_name
    session["user_id"] = company.add_customer(user_name, password)
    user_id = company.add_customer(user_name, password)
    return Redirect ("/user_profile")
@rt("/login")
def register():
    return Html(
        Body(
            Link(rel="stylesheet", href="/static/style.css"),
            Div(
                Div(
                    H1("Login", _class="title"),
                    Form(
                        Div(
                            Input(type="text", name="user_name", placeholder="", required=True, _class="input"),
                            Div(_class="cut"),
                            Label("User Name", _class="placeholder", _for="User Name"),
                            _class="input-container ic1"
                            
                        ),
                        Div(
                            Input(type="password", name="password", placeholder="", required=True, _class="input"),
                            Div(_class="cut cut-short"),
                            Label("Password", _class="placeholder", _for="Password"),
                            _class="input-container ic2"
                        ),
                         Div(  
                        Button("Sign Up", type="submit", _class="submit"),
                        Button("Home", type="button", _class="submit home-btn", onclick="window.location.href='/'"),
                        _class="button-group"
                    ),
                    method="post", action="/process_login",
                    _class="form-box",
                    ),
                    
                )
            )
        )
    )
 
@rt("/process_login")
def process_login(user_name: str = None, password: str = None):
    print(f"DEBUG: login request user_name={user_name}, password={password}")  

    if not user_name or not password:
        return Redirect ("/show_invalid")

    user = company.authenticate(user_name, password)
    if user:
        session["user_name"] = user.user_name  
        session["user_id"] = user.user_id
        print(f"DEBUG: session = {session}")  #
        return Redirect("/user_profile")
    else:
        return Redirect("/show_l")

@rt("/logout")
def logout():
    session.clear() 
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/login.css")
        ),
        Body(
            Div(
                H1("logout", _class="invalid-title"),
                P("ขอบคุณที่ใช้บิรการค่ะ", _class="invalid-text"),
                Button("กลับไปหน้าหลัก", _class="invalid-btn", onclick="window.location.href='/'"),
                _class="invalid-container"
            )
        )
    )


@rt("/bus_schedule")
def bus_schedule():
    schedules = company.schedules  

    if not schedules:
        return Html(Body(P("❌ ไม่พบตารางเดินรถ!", _class="error"), A("กลับหน้าหลัก", href="/")))

    user_name = session.get("user_name")  # เช็คว่าผู้ใช้ล็อกอินหรือไม่

    return Html(
        Head(
            Link(rel="stylesheet", href="/static/schedule.css")
        ),
        Body(
            Div(
                H1("🚌 ตารางเดินรถ", _class="title"),
                Table(
                    Tr(
                        Th("🆔 รหัสตาราง", _class="table-header"),
                        Th("📍 ต้นทาง - ปลายทาง", _class="table-header"),
                        Th("💰 ราคา", _class="table-header"),
                        Th("🚌 จำนวนรถ", _class="table-header"),
                        Th("🎟️ จองตั๋ว", _class="table-header"),
                    ),
                    *[
                        Tr(
                            Td(s.schedule_id, _class="schedule-id"),
                            Td(f"{s.route}", _class="schedule-route"),
                            Td(f"{s.ticket_price} Baht", _class="schedule-price"),
                            Td(f"{len(s.buses)} คัน", _class="schedule-buses"),
                            Td(Button("🛒 จองตั๋ว", _class="book-btn",
                                      onclick=f"window.location.href='/select_bus?schedule_id={s.schedule_id}'"))
                        )
                        for s in schedules
                    ],
                    _class="bus-table"
                ),
                Div(
                    Button("🏠 HOME", _class="home-btn", onclick="window.location.href='/';"),
                    Button("🎫 ดูตั๋วของฉัน", _class="home-btn", onclick="window.location.href='/view_tickets';") if user_name else "",
                    _class="button-group"
                ),
                _class="schedule-container"
            )
        )
    )


@rt("/select_bus")
def select_bus(schedule_id: str = None):
    schedule = company.schedule_select(schedule_id)
    if not schedule:
        return Html(Body(P("❌ ไม่พบตารางเดินรถ!"), A("กลับหน้าหลัก", href="/")))

    return Html(
        Head(
            Link(rel="stylesheet", href="/static/select_bus.css")
        ),
        Body(
            Div(
                H1(f"🚌 เลือกรถบัสสำหรับเส้นทาง {schedule.route}", _class="title"),
                Div(
                    *[
                        Div(
                            H2(bus.bus_name, _class="bus-name"),
                            P(f"🪑 ที่นั่งว่าง: {bus.available_seat} ที่นั่ง", _class="bus-seats"),
                            Button("🎟️ เลือก", _class="select-btn",
                                   onclick=f"window.location.href='/select_seat?schedule_id={schedule_id}&bus_plate={bus.license_plate}'"),
                            _class="bus-card"
                        )
                        for bus in schedule.buses
                    ],
                    _class="bus-container"
                ),
                A("🔙 ย้อนกลับ", href=f"/bus_schedule", _class="back-btn"),
                _class="select-bus-container"
            )
        )
    )



# @rt("/select_bus")
# def select_bus(schedule_id: str = None):
#     schedule = company.schedule_select(schedule_id)
#     if not schedule:
#         return Html(Body(P("❌ ไม่พบตารางเดินรถ!"), A("กลับหน้าหลัก", href="/")))

#     return Html(
#         Body(
#             H2(f"เลือกรถสำหรับเส้นทาง {schedule.route}"),
#             Table(
#                 Tr(Th("ชื่อรถ"), Th("ที่นั่งว่าง"), Th("เลือก")),
#                 *[
#                     Tr(Td(b.bus_name), Td(f"{b.available_seat} ที่นั่ง"),
#                         Td(Button("เลือก", onclick=f"window.location.href='/select_seat?schedule_id={schedule_id}&bus_plate={b.license_plate}'")))
#                     for b in schedule.buses
#                 ],
#             ),
#             A("ย้อนกลับ", href="/")
#         )
#     )
@rt("/select_seat")
def select_seat(schedule_id: str = None, bus_plate: str = None):
    if "user_name" not in session:
        return Redirect("/show_ar")
    bus = company.get_bus(schedule_id, bus_plate)
    if not bus:
        return Html(Body(P("❌ ไม่พบรถบัสที่คุณเลือก"), A("Go to Home", href="/")))

    return Html(
        Head(
            Link(rel="stylesheet", href="/static/select_seat.css")
        ),
        Body(
            Div(
                H1(f"💺 เลือกที่นั่งสำหรับ {bus.bus_name}", _class="title"),
                Div(
                    *[
                        Button(str(seat), _class="seat-btn available",
                               onclick=f"window.location.href='/book_seat?schedule_id={schedule_id}&bus_plate={bus_plate}&seat_number={seat}'")
                        if seat in bus.seat_list else
                        Button(str(seat), _class="seat-btn booked", disabled=True)
                        for seat in range(1, bus.available_seat + 1)
                    ],
                    _class="seat-container"
                ),
                A("🔙 ย้อนกลับ", href=f"/select_bus?schedule_id={schedule_id}", _class="back-btn"),
                _class="select-seat-container"
            )
        )
    )
@rt("/show_ar")
def show_invalid():
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/invalid.css")
        ),
        Body(
            Div(
                H1("❌ ขออภัย! คุณไม่มีสิทธิ์เข้าถึงหน้านี้ ❌", _class="invalid-title"),
                P("กรุณาสมัครสมาชิกก่อน", _class="invalid-text"),
                 P("หรือสมัครสมาชิกก่อน", _class="invalid-text"),
                Button("กลับไปหน้าหลัก", _class="invalid-btn", onclick="window.location.href='/'"),
                _class="invalid-container"
            )
        )
    )
# @rt("/select_seat")
# def select_seat(schedule_id: str = None, bus_plate: str = None):
#     if "user_name" not in session:
#         return Html(Body(P("⚠️ กรุณาล็อคอินก่อนนะ"), A("Go to Login", href="/login")))

#     bus = company.get_bus(schedule_id, bus_plate)
#     if not bus:
#         return Html(Body(P("❌ ไม่พบรถบัสที่คุณเลือก"), A("Go to Home", href="/")))

#     return Html(
#         Body(
#             H2(f"เลือกที่นั่งสำหรับ {bus.bus_name}"),
#             Table(
#                 Tr(*[Td(Button(str(seat), onclick=f"window.location.href='/book_seat?schedule_id={schedule_id}&bus_plate={bus_plate}&seat_number={seat}'"))
#                     for seat in bus.seat_list]),
#             ),
#             A("ย้อนกลับ", href=f"/select_bus?schedule_id={schedule_id}")
#         )
#     )

# @rt("/book_seat")
# def book_seat(schedule_id: str = None, bus_plate: str = None, seat_number: int = None):
#     if "user_name" not in session:
#         return Html(Body(P("⚠️ ต้องล็อคอินก่อนนะ"), A("Go to Login", href="/login")))

#     customer_id = session.get("user_id")
#     booking_message = company.book_seat(customer_id, schedule_id, bus_plate, seat_number)

#     return Html(Body(
#         P(booking_message),
#         Div(A("Go to Home", href="/")),
#         Div(A("Payment", href="/pay_booking"), style="margin-top: 20px;")
#     ))
@rt("/book_seat")
def book_seat(schedule_id: str = None, bus_plate: str = None, seat_number: int = None):
    customer_name = session.get("user_name")
    if not customer_name:
        return booking_status_page(False, "❌ ต้องล็อคอินก่อนนะ! 🔑 กรุณาเข้าสู่ระบบก่อนทำการจองที่นั่ง")

    customer = company.get_customer_by_name(customer_name)
    if not customer:
        return booking_status_page(False, "❌ ไม่พบบัญชีลูกค้า กรุณาลองใหม่")

    booking_message = company.book_seat(customer.user_id, schedule_id, bus_plate, seat_number)
    success = "successfully" in booking_message

    return booking_status_page(success, booking_message, seat_number)

def booking_status_page(success: bool, message: str, seat_number: int = None):
    return Html(
        Head(Link(rel="stylesheet", href="/static/booking_status.css")),
        Body(
            Div(
                Div(
                    H1("📌 สถานะการจอง", _class="booking-title"),
                    P(message, _class="booking-message"),
                    Div(
                        A("🏠 กลับหน้าหลัก", href="/", _class="btn-home"),
                        A("💳 จ่ายเงิน", href=f"/process_payment?seat_number={seat_number}", _class="btn-pay"),
                        A("🎫 ดูตั๋วของฉัน", href="/view_tickets", _class="btn-ticket"),
                        _class="button-group"
                    ),
                    _class="booking-card success" if success else "booking-card failed"
                ),
                _class="booking-container"
            )
        )
    )


#     ))
# @rt("/book_seat")
# def book_seat(schedule_id: str = None, bus_plate: str = None, seat_number: int = None):
#     if "user_name" not in session:
#     return Html(Body(P("⚠️ ต้องล็อคอินก่อนนะ"), A("🔑 เข้าสู่ระบบ", href="/login", _class="btn-login")))

#         customer_id = session.get("user_id")
#         booking_message = company.book_seat(customer_id, schedule_id, bus_plate, seat_number)

#         success = "สำเร็จ" in booking_message  # เช็คว่าการจองสำเร็จหรือไม่

#         return Html(
#             Head(
#                 Link(rel="stylesheet", href="/static/booking.css")
#             ),
#             Body(
#                 Div(
#                     H1("✅ การจองสำเร็จ!", _class="success-title") if success else H1("❌ Booking Failed!", _class="fail-title"),
#                     P(booking_message, _class="message"),
#                     Div(
#                         A("🎟️ ดูตั๋วของฉัน", href="/view_tickets", _class="btn-ticket"),
#                         A("🏠 กลับหน้าหลัก", href="/", _class="btn-home"),
#                         _class="button-group"
#                     ),
#                     _class="booking-container"
#                 )
#             )
#         )


@rt("/process_payment")
def process_payment(seat_number: int = None):
    print(f"DEBUG: session = {session}")  # ✅ Debug session
    if "user_name" not in session:  
        print(session)
        return Html(Body(P("⚠️ กรุณาล็อคอินก่อนนะ"), A("Go to Login", href="/login")))

    customer_id = session.get("user_id")
    print(f"DEBUG: customer_id = {customer_id}")  # ✅ Debug user_id

    if not customer_id:
        return Redirect("/show_ar")

    ticket, message = company.process_payment(customer_id, seat_number)

    if not ticket:
        return Html(Body(P(message), A("Go Back", href="/pay_booking")))

    return Redirect("/payment_success")
@rt("/payment_success")
def payment_success(ticket_id: str = None, seat_number: int = None, issued_date: str = None):
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/payment_success.css")
        ),
        Body(
            Div(
                Div(
                    H1("✅ ชำระเงินสำเร็จ!", _class="success-title"),
                    P(f"ที่นั่ง  ได้รับการจองเรียบร้อยแล้ว", _class="seat-info"),
                    Div(
                        P("🎟️ Ticket ID:", _class="ticket-label"),
                        Span(ticket_id, _class="ticket-id")
                    ),
                    Div(
                        P("📅 ออกตั๋วเมื่อ:", _class="date-label"),
                        Span(issued_date, _class="date-info")
                    ),
                    Div(
                        A("🎫 ดูตั๋วของฉัน", href="/view_tickets", _class="btn ticket-btn"),
                        A("🏠 กลับหน้าหลัก", href="/", _class="btn home-btn"),
                        _class="button-group"
                    ),
                    _class="payment-card"
                ),
                _class="payment-container"
            )
        )
    )
@rt("/view_tickets")
def view_tickets():
    """ แสดงรายการตั๋วของผู้ใช้ที่ล็อกอิน """
    if "user_name" not in session:
        return Redirect ("/show_ar")

    customer_id = session.get("user_id")  
    tickets = company.view_ticket(customer_id)  

    if not tickets or tickets == ["❌ ไม่มีตั๋วที่ออกในระบบ"]:
        return Html(
            Head(Link(rel="stylesheet", href="/static/view_tickets.css")),
            Body(
                Div(
                    H1("🎟️ ตั๋วของฉัน", _class="ticket-title"),
                    P("❌ ไม่มีตั๋วที่ออกในระบบ", _class="no-ticket"),
                    A("🏠 กลับหน้าหลัก", href="/", _class="btn home-btn"),
                    _class="ticket-container empty"
                )
            )
        )

    return Html(
        Head(Link(rel="stylesheet", href="/static/view_tickets.css")),
        Body(
            Div(
                H1("🎟️ ตั๋วของฉัน", _class="ticket-title"),
                Div(
                    *[
                        Div(
                            P(f"🎫 Ticket ID: {ticket.split(', ')[0]}", _class="ticket-id"),
                            P(f"💺 ที่นั่ง: {ticket.split(', ')[1]}", _class="seat-info"),
                            P(f"📅 ออกตั๋วเมื่อ: {ticket.split(', ')[2]}", _class="date-info"),
                            Div(
                                A("🔄 ขอคืนเงิน", href=f"/refund_ticket?ticket_id={ticket.split(', ')[0]}", _class="btn refund-btn"),
                                _class="button-group"
                            ),
                            _class="ticket-card"
                        )
                        for ticket in tickets
                    ],
                    _class="ticket-list"
                ),
                A("🏠 กลับหน้าหลัก", href="/", _class="btn home-btn"),
            
                _class="ticket-container"
            )
        )
    )


@rt("/refund_ticket")
def refund_ticket(ticket_id: str = None):
    """ ดำเนินการขอคืนเงิน """
    if "user_name" not in session:
        return Redirect ("/show_ar")

    customer_id = session.get("user_id")
    ticket, message = company.refund_ticket(customer_id, ticket_id)

    if not ticket:
        return Html(Body(P(message), A("Go Back", href="/view_tickets")))

    return Html(
        Head(Link(rel="stylesheet", href="/static/refund_success.css")),
        Body(
            Div(
                Div(
                    H1("✅ คืนเงินสำเร็จ!", _class="refund-title"),
                    P(f"🎫 Ticket ID: {ticket.ticket_id} ถูกยกเลิกแล้ว", _class="refund-message"),
                    Div(
                        A("🎟️ ดูตั๋วของฉัน", href="/view_tickets", _class="btn ticket-btn"),
                        A("🏠 กลับหน้าหลัก", href="/", _class="btn home-btn"),
                        _class="button-group"
                    ),
                    _class="refund-card"
                ),
                _class="refund-container"
            )
        )
    )

serve()
