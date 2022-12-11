from tkinter import messagebox
import re
from tkinter import *
from pages import Login


class Register:
    email_regex = re.compile(r"^[^@]+@[^.]+\..+$")

    def __init__(self) -> None:
        self.password_regex = re.compile(r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])(?=.*[!@#$%^&*]).{12,}$")

        self.root = Tk()
        self.root.title("Registration")

        self.email_label = Label(self.root, text="Email:")
        self.email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.root)
        self.email_entry.grid(row=0, column=1)

        self.password_label = Label(self.root, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.password_verify_label = Label(self.root, text="Verify password:")
        self.password_verify_label.grid(row=2, column=0)
        self.password_verify_entry = Entry(self.root, show="*")
        self.password_verify_entry.grid(row=2, column=1)
        self.submit_button = Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=0)
        self.cancel_button = Button(self.root, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=3, column=1)

    def show_login_page(self) -> None:
        self.root.destroy()
        login = Login()
        login.root.mainloop()

    def submit(self) -> None:
        password = self.password_entry.get()
        password_verify = self.password_verify_entry.get()

        email_regex = re.compile(r"^[^@]+@[^.]+\..+$")

        email = self.email_entry.get()

        if not email_regex.match(email):
            messagebox.showerror("Error", "Invalid email format. Please enter a valid email.")
            return

        if password != password_verify:
            messagebox.showerror("Error", "Your passwords don't match.")
            return
        elif not self.password_regex.match(password):
            messagebox.showerror("Error", "Your password must be at least 12 characters long, "
                                          "and must contain at least one capital letter, one number, and one symbol.")
            return

        messagebox.showinfo("Success", "Registration successful!")
        self.show_login_page()

    def cancel(self) -> None:
        self.root.destroy()
        login_reconstruct = Login()
        login_reconstruct.root.mainloop()

    def show_register_page(self) -> None:
        self.root.mainloop()
