import ctypes
import re
from tkinter import *

import firebase_admin
import phonenumbers
from firebase_admin import auth
from firebase_admin import credentials

cred = credentials.Certificate('auth-python-12139-firebase-adminsdk-1y5gj-da7bb50334.json')
firebase_admin.initialize_app(cred)
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class Registration(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1380x768")
        self.title("Registration Page")

    def Label(self):
        self.backGroundImage = PhotoImage(file="images/register_page.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

    def Entry(self):
        self.email = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.email.place(x=549, y=335, width=350, height=24)

        self.confirm_email = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.confirm_email.place(x=620, y=379, width=275, height=24)

        self.phone_number = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.phone_number.place(x=623, y=424, width=272, height=24)

    def Button(self):
        self.loginButtonImage = PhotoImage(file="images/register_button.png")
        self.loginButton = Button(self, image=self.loginButtonImage, command=self.Register, border=0)
        self.loginButton.place(x=803, y=469)

        self.toLoginImage = PhotoImage(file="images/txt_login.png")
        self.toLoginButton = Button(self, image=self.toLoginImage, command=self.unHideLogin, font="25", border=0)
        self.toLoginButton.place(x=574, y=540)

    def unHideLogin(self):
        Login.deiconify()
        Registration.destroy(self)

    def Register(self):
        """THIS IS WHERE THE REGISTRATION HAPPENS"""
        Email = self.email.get()
        Confirm_Email = self.confirm_email.get()
        Phone_Number = self.phone_number.get()

        if re.search(regex, Email):
            print("Email is valid")
            if Email == Confirm_Email:
                print("Emails match")
                if phonenumbers.is_possible_number(phonenumbers.parse(Phone_Number)):
                    print("Phone number exists")
                    user = auth.create_user(email=Email, phone_number=Phone_Number)
                    print("User created successfully! Users ID is: {0}".format(user.uid))
                else:
                    print("Phone number does not exist!")
                    ctypes.windll.user32.MessageBoxW(0, "Phone number does not exist!", "Error", 0)
            else:
                print("Emails do not match")
                ctypes.windll.user32.MessageBoxW(0, "Entered email addresses do not match!", "Error", 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Entered email is not valid!", "Error", 0)
            print("Email is not valid")


def callRegistration():
    Login.withdraw()
    registration = Registration()
    registration.grab_set()
    registration.Label()
    registration.Entry()
    registration.Button()
    registration.mainloop()


def callWorkout():
    Login.withdraw()
    workout = Workout()
    workout.grab_set()
    workout.Label()
    workout.mainloop()


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1380x768")
        self.title("Login Page")

    def Label(self):
        self.log_backGroundImage = PhotoImage(file="images/login_page.png")
        self.log_backGroundImageLabel = Label(self, image=self.log_backGroundImage)
        self.log_backGroundImageLabel.place(x=0, y=0)

    def Entry(self):
        self.log_email = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.log_email.place(x=550, y=379, width=335, height=24)

        self.log_phoneNumber = Entry(self, borderwidth=0, highlightthickness=0, font="25")
        self.log_phoneNumber.place(x=625, y=441, width=270, height=24)

    def Button(self):
        self.loginButtonImage = PhotoImage(file="images/login_button.png")
        self.loginButton = Button(self, image=self.loginButtonImage, command=self.Log, border=0)
        self.loginButton.place(x=803, y=483)

        self.toRegisterImage = PhotoImage(file="images/txt_register.png")
        self.toRegisterButton = Button(self, image=self.toRegisterImage, command=callRegistration, font="25", border=0)
        self.toRegisterButton.place(x=585, y=531)


    def Log(self):
        Login_email = self.log_email.get()
        Login_PhoneNumber = self.log_phoneNumber.get()

        if Login_email != "" and re.search(regex, Login_email):
            checkUser = auth.get_user_by_email(Login_email)
            if len(checkUser.uid) == 28:
                print("User exists, his ID is: ", checkUser.uid)
                callWorkout()
        elif Login_PhoneNumber != "" and phonenumbers.is_possible_number(phonenumbers.parse(Login_PhoneNumber)):
            checkUser = auth.get_user_by_phone_number(Login_PhoneNumber)
            if len(checkUser.uid) == 28:
                print("User exists, his ID is: ", checkUser.uid)
                callWorkout()
        else:
            print("Please enter a valid email or a password!")
            ctypes.windll.user32.MessageBoxW(0, "Please enter a valid email or a password!", "Error", 0)


class Workout(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1380x768")
        self.title("Login Page")

    def Label(self):
        self.log_backGroundImage = PhotoImage(file="images/wo_bg_page.png")
        self.log_backGroundImageLabel = Label(self, image=self.log_backGroundImage)
        self.log_backGroundImageLabel.place(x=0, y=0)

    def Button(self):
        self.warrPose = PhotoImage(file="images/warrior_pose.png")
        self.warrButton = Button(self, image=self.warrPose, border=0)
        self.warrButton.place(x=39, y=184)

        self.dogPose = PhotoImage(file="images/downward_facing_dog.png")
        self.dogButton = Button(self, image=self.dogPose, border=0)
        self.dogButton.place(x=39, y=476)

        self.bicepCurl = PhotoImage(file="images/bicep_curl.png")
        self.bicepButton = Button(self, image=self.bicepCurl, border=0)
        self.bicepButton.place(x=731, y=184)

        self.overheadPress = PhotoImage(file="images/overhead_press.png")
        self.overheadButton = Button(self, image=self.overheadPress, border=0, bg=None)
        self.overheadButton.place(x=731, y=476)


if __name__ == "__main__":

    #Login = Login()
    #Login.Label()
    #Login.Entry()
    #Login.Button()
    #Login.mainloop()

    workout = Workout()
    workout.Label()
    workout.Button()
    workout.mainloop()