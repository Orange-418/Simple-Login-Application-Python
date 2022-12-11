from tkinter import messagebox
import re
from typing import Optional
from tkinter import *
from emailchecker import User
from pages import Register


class Login:
    def __init__(self, user: Optional[User] = None) -> None:
        self.user = user
        self.root = Tk()
        self.root.title("Login")

        self.email_label = Label(self.root, text="Email:")
        self.email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.root)
        self.email_entry.grid(row=0, column=1)

        self.password_label = Label(self.root, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0)
        self.register_button = Button(self.root, text="Register", command=self.register)
        self.register_button.grid(row=2, column=1)

    def login(self) -> None:
        password = self.password_entry.get()
        email_regex = re.compile(r"^[^@]+@[^.]+\..+$")
        email = self.email_entry.get()

        if not email_regex.match(email):
            messagebox.showerror("Error", "Invalid email format. Please enter a valid email.")
            return

        if self.user and self.user.email == email and self.user.password == password:
            self.root.destroy()
            register = Register()
            register.show_register_page()
        else:
            messagebox.showerror("Error", "Invalid email or password. Please try again.")

    def register(self) -> None:
        self.root.destroy()
        register = Register()
        register.show_register_page()
