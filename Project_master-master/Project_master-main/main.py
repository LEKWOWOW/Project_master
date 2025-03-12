from fasthtml.common import *
import os

#ไม่อ่านคอมเน็ตแต่มานั่งทำหมอนี่ เท่ชะมัด
ACCOUNT_FILE = 'accounts.py'

def load_accounts():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, 'r') as file:
            return eval(file.read())
    return {}

def save_accounts(accounts):
    with open(ACCOUNT_FILE, 'w') as file:
        file.write(str(accounts))

class Company:
    def __init__(self):
        self.accounts = load_accounts()
        self.current_user = None

    def register(self, email, password):
        if email in self.accounts:
            return False
        self.accounts[email] = password
        save_accounts(self.accounts)
        return True

    def login(self, email, password):
        if self.accounts.get(email) == password:
            self.current_user = email
            return True
        return False

company = Company()

app, rt = fast_app()

@rt("/")
def home():
    return Html(
        Body(
            H1("Welcome to Bus Booking System 🚌"),
            A("Login", href="/login"),
            A("Register", href="/register")
        )
    )

@rt("/register")
def register_page():
    return Html(
        Body(
            H2("Register"),
            Form(
                Input(type="email", name="email", placeholder="Email", required=True),
                Input(type="password", name="password", placeholder="Password", required=True),
                Button("Register", type="submit"),
                method="post", action="/do_register"
            ),
            A("Back", href="/")
        )
    )

@rt("/do_register")
def do_register(email: str, password: str):
    if company.register(email, password):
        return Redirect("/login")
    return Html(Body(P("Account already exists."), A("Try again", href="/register")))

@rt("/login")
def login_page():
    return Html(
        Body(
            H2("Login"),
            Form(
                Input(type="email", name="email", placeholder="Email", required=True),
                Input(type="password", name="password", placeholder="Password", required=True),
                Button("Login", type="submit"),
                method="post", action="/do_login"
            ),
            A("Back", href="/")
        )
    )

@rt("/do_login")
def do_login(email: str, password: str):
    if company.login(email, password):
        return Html(Body(P(f"Logged in as {email}"), A("Go to Home", href="/")))
    return Html(Body(P("Login failed."), A("Try again", href="/login")))

serve()