import ctypes
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from tkinter import *
import re

from google.auth.transport import requests

cred = credentials.Certificate('auth-python-12139-firebase-adminsdk-1y5gj-da7bb50334.json')

firebase_admin.initialize_app(cred)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

currentPage = "login"
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


class Registration(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1380x768")

    def Label(self):
        self.backGroundImage = PhotoImage(file="register_page_1.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

    def Entry(self):
        self.email = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.email.place(x=550, y=379, width=335, height=24)

        self.password = Entry(self, borderwidth=0, show="*", highlightthickness=0, font="25")
        self.password.place(x=585, y=431, width=300, height=24)

        self.password_confirm = Entry(self, borderwidth=0, show="*", highlightthickness=0, font="25")
        self.password_confirm.place(x=655, y=483, width=230, height=24)

    def Button(self):
        self.loginButtonImage = PhotoImage(file="register_button.png")
        self.loginButton = Button(self, image=self.loginButtonImage, command=self.Register, border=0)
        self.loginButton.place(x=803, y=529)

    def Register(self):
        """THIS IS WHERE THE REGISTRATION HAPPENS"""
        Email = self.email.get()
        Password = self.password.get()
        Password_confirm = self.password_confirm.get()

        if re.search(regex, Email):
            print("Email is valid")
            if len(Password) < 6:
                ctypes.windll.user32.MessageBoxW(0, "Entered password is too weak!", "Error", 0)
                print("Password is too weak")
            else:
                print("Password is good")
                if Password == Password_confirm:
                    print("Passwords match")
                    user = auth.create_user(email=Email, password=Password)
                    print("User created successfully! Users ID is: {0}".format(user.uid))
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Passwords do not match!", "Error", 0)
                    print("Passwords do not match")
        else:
            ctypes.windll.user32.MessageBoxW(0, "Entered email is not valid!", "Error", 0)
            print("Email is not valid")


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1380x768")

    def Label(self):
        self.log_backGroundImage = PhotoImage(file="login_page_1.png")
        self.log_backGroundImageLabel = Label(self, image=self.log_backGroundImage)
        self.log_backGroundImageLabel.place(x=0, y=0)

    def Entry(self):
        self.log_email = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.log_email.place(x=550, y=379, width=335, height=24)

        self.log_password = Entry(self, borderwidth=0, show="*", highlightthickness=0, font="25")
        self.log_password.place(x=585, y=431, width=300, height=24)

    def Button(self):
        self.loginButtonImage = PhotoImage(file="login_button.png")
        self.loginButton = Button(self, image=self.loginButtonImage, command=self.Log, border=0)
        self.loginButton.place(x=803, y=483)

    def Log(self):
        Login_email = self.log_email.get()
        Login_password = self.log_password.get()

        checkUser = auth.get_user_by_email(Login_email)
        print(checkUser.uid)



if __name__ == "__main__":
    '''
    Login = Login()
    Login.Label()
    Login.Entry()
    Login.Button()
    '''

    '''THIS IS FOR THE REGISTRATION PAGE'''
    Registration = Registration()
    Registration.Label()
    Registration.Entry()
    Registration.Button()    

    Registration.mainloop()
