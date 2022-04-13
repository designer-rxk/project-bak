import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from tkinter import *
import re

cred = credentials.Certificate('auth-python-12139-firebase-adminsdk-1y5gj-da7bb50334.json')

firebase_admin.initialize_app(cred)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1380x768")

    def Label(self):
        self.backGroundImage = PhotoImage(file="login_background.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        self.title = Label(self, text="project-b", font="Futura-Heavy 60")
        self.title.place(x=542, y=169)

        self.title = Label(self, text="register", font="Futura-Heavy 20")
        self.title.place(x=650, y=280)

        self.title = Label(self, text="email:", font="Futura-Heavy 15")
        self.title.place(x=475, y=377)

        self.title = Label(self, text="password:", font="Futura-Heavy 15")
        self.title.place(x=475, y=429)

        self.title = Label(self, text="confirm password:", font="Futura-Heavy 15")
        self.title.place(x=475, y=481)

    def Entry(self):
        self.email = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.email.place(x=535, y=377, width=370, height=31)

        self.password = Entry(self, borderwidth=0, show="*", highlightthickness=0, font="25")
        self.password.place(x=570, y=429, width=335, height=31)

        self.password_confirm = Entry(self, borderwidth=0, show="*", highlightthickness=0, font="25")
        self.password_confirm.place(x=640, y=481, width=265, height=31)

    def Button(self):
        self.loginButtonImage = PhotoImage(file="login_button.png")
        self.loginButton = Button(self, image=self.loginButtonImage, command=self.Output, border=0)
        self.loginButton.place(x=803, y=529)

    def Output(self):
        """THIS IS WHERE THE REGISTRATION HAPPENS"""
        Email = self.email.get()
        Password = self.password.get()
        Password_confirm = self.password_confirm.get()

        if re.search(regex, Email):
            print("Email is valid")
        else:
            print("Email is not valid")

        if len(Password) < 6:
            print("Password is too weak")
        else:
            print("Password is good")

        if Password == Password_confirm:
            print("Passwords match")
        else:
            print("Passwords do not match")

        if Password == Password_confirm:
            user = auth.create_user(email=Email, password=Password)

            print("User created successfully! Users ID is: {0}".format(user.uid))
        else:
            print("Failed to create a user!")


if __name__ == "__main__":
    Login = login()
    Login.Label()
    Login.Entry()
    Login.Button()
    Login.mainloop()
