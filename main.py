from pages import Login


# The main.py file simply creates an instance of the Login class
# and calls the show_login_page method to display the login window.
def main() -> None:
    login = Login()
    login.root.mainloop()


if __name__ == "__main__":
    main()
