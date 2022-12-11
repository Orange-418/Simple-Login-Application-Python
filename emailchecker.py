from tkinter import messagebox
import re


class User:
    email_regex = re.compile(r"^[^@]+@[^.]+\..+$")

    def __init__(self, email: str, password: str) -> None:
        if not self.email_regex.match(email):
            messagebox.showerror("Error", "Invalid email format. Please enter a valid email.")
            raise ValueError("Invalid email format. Please enter a valid email.")

        self.email = email
        self.password = password
