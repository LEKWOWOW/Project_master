from fasthtml.common import *
from create_instance import company
app, rt = fast_app()

@rt("/")
def home():
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

@rt("/process_register")
def process_register(user_name: str = None, password: str = None):
    if not user_name or not password:
        return Html(Body(P("❌ Missing username or password!"), A("Try Again", href="/register")))
    
    existing_user = company.get_customer_by_name(user_name)
    if existing_user:
        return Html(Body(P("⚠️ This username is already taken! Please choose another."), A("Try Again", href="/register")))
    
    user_id = company.add_customer(user_name, password)
    print(f"user_name: {user_name}, password: {password}")
    return Html(Body(P(f"✅ Registration Successful! Your User ID: {user_id}"), A("Go to Login", href="/login")))

@rt("/login")
def login():
    return Html(
        Body(
            H2("Login"),
            Form(
                Input(type="text", name="name", placeholder="name", required=True),
                Input(type="password", name="password", placeholder="Password", required=True),
                Button("Login", type="submit"),
                method="post", action="/process_login"
            )
        )
    )

@rt("/process_login")
def process_login(name: str = None, password: str = None):
    if not name or not password:
        return Html(Body(P("❌ Missing user ID or password!"), A("Try Again", href="/login")))
    
    user = company.authenticate(name, password)
    if user:
        return Html(Body(P(f"✅ Login Successful! Welcome {user.user_name}"), A("Go to Home", href="/")))
    else:
        return Html(Body(P("❌ Invalid User ID or Password!"), A("Try Again", href="/login")))

serve()
