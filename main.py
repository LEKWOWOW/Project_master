from fasthtml.common import *
from create_instance import company
app, rt = fast_app()
session = {}



@rt("/")
def home():
    user_name = session.get("user_name")
    if user_name:
        return Html(
            Body(
                H1(f"Welcome, {user_name} 🚌"),
                H2("Available Bus Schedules"),
                Table(
                    Tr(Th("Schedule ID"), Th("Route"), Th("Price"), Th("Actions")),
                    *[Tr(Td(s.schedule_id), Td(s.route), Td(f"{s.ticket_price} Baht"),
                        Td(Button("Select", onclick=f"window.location.href='/select_bus?schedule_id={s.schedule_id}'")))
                      for s in company.schedules],
                ),
                Div(
                    Button("Logout", onclick="window.location.href='/logout'", style="width: 200px; height: 30px;")
                )
            )
        )
    else:
        return Html(
            Body(
                H1("Welcome to Bus Booking System 🚌"),
                Div(
                    Button(B("HOME"), style="width: 200px; height: 30px;"),
                    Button(B("LOGIN"), onclick="window.location.href='/login'", style="width: 200px; height: 30px;"),
                    Button(B("REGISTER"), onclick="window.location.href='/register'", style="width: 200px; height: 30px;")
                )
            )
        )


@rt("/register")
def register():
    return Html(
        Body(
            H2("Register"),
            Form(
                Input(type="text", name="user_name", placeholder="Full Name", required=True),
                Input(type="password", name="password", placeholder="Password", required=True),
                Button("Sign Up", type="submit"),
                method="post", action="/process_register"
            )
        )
    )
@rt("/process_login")
def process_login(user_name: str = None, password: str = None):
    if not user_name or not password:
        return Html(Body(P("❌ Missing user name or password!"), A("Try Again", href="/login")))
    
    user = company.authenticate(user_name, password)
    if user:
        session["user_name"] = user.user_name
        session["user_id"] = user.user_id
        return Html(Body(P(f"✅ Login Successful! Welcome {user.user_name}"), A("Go to Home", href="/")))
    else:
        return Html(Body(P("❌ Invalid User Name or Password!"), A("Try Again", href="/login")))

@rt("/process_register")
def process_register(user_name: str = None, password: str = None):
    if not user_name or not password:
        return Html(Body(P("❌ Missing username or password!"), A("Try Again", href="/register")))
    
    existing_user = company.get_customer_by_name(user_name)
    if existing_user:
        return Html(Body(P("ชื่อนี้มีคนใช้ไปแล้วนะสุดหล่อ."), A("Try Again", href="/register")))
    
    user_id = company.add_customer(user_name, password)
    return Html(Body(P(f"✅ สมัครได้แล้วนะจะ ID: {user_id}"), A("Go to Login", href="/login")))

@rt("/login")
def login():
    return Html(
        Body(
            H2("Login"),
            Form(
                Input(type="text", name="user_name", placeholder="User Name", required=True),
                Input(type="password", name="password", placeholder="Password", required=True),
                Button("Login", type="submit"),
                method="post", action="/process_login"
            )
        )
    )


@rt("/logout")
def logout():
    session.clear() 
    return Html(Body(P("✅ Logged out successfully!"), A("Go to Home", href="/")))

@rt("/select_bus")
def select_bus(schedule_id: str = None):
    schedule = company.schedule_select(schedule_id)
    if not schedule:
        return Html(Body(P("❌ Schedule not found!"), A("Go to Home", href="/")))

    return Html(
        Body(
            H2(f"Select Bus for {schedule.route}"),
            Table(
                Tr(Th("Bus Name"), Th("Available Seats"), Th("Actions")),
                *[
                    Tr(Td(b.bus_name), Td(f"{b.available_seat} seats"),
                        Td(Button("Select", onclick=f"window.location.href='/select_seat?schedule_id={schedule_id}&bus_plate={b.license_plate}'")))
                    for b in schedule.buses
                ],
            ),
            A("Go Back", href="/")
        )
    )
@rt("/select_seat")
def select_seat(schedule_id: str = None, bus_plate: str = None):
    if "user_name" not in session:
        return Html(Body(P("⚠️ กรุณาล็อคอินก่อนนะ"), A("Go to Login", href="/login")))

    bus = company.get_bus(schedule_id, bus_plate)
    if not bus:
        return Html(Body(P("❌ หารถไม่เจอถ้าไม่เจอส่วนมาคือเว็บมัคแดกไปละ"), A("Go to Home", href="/")))

    return Html(
        Body(
            H2(f"Select Seat for {bus.bus_name}"),
            Table(
                Tr(*[Td(Button(str(seat), onclick=f"window.location.href='/book_seat?schedule_id={schedule_id}&bus_plate={bus_plate}&seat_number={seat}'"))
                    for seat in bus.seat_list]),
            ),
            A("Go Back", href=f"/select_bus?schedule_id={schedule_id}")
        )
    )




@rt("/book_seat")
def book_seat(schedule_id: str = None, bus_plate: str = None, seat_number: int = None):
    if "user_name" not in session:
        return Html(Body(P("⚠️ ต้องล็อคอินก่อนนะ"), A("Go to Login", href="/login")))

    customer_id = session.get("user_id")
    booking_message = company.book_seat(customer_id, schedule_id, bus_plate, seat_number)

    return Html(Body(
        P(booking_message),
        A("Go to Home", href="/")
    ))



serve()
