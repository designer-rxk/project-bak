import ctypes
import re
from tkinter import *
import cv2
import mediapipe as mp
import numpy as np

import firebase_admin
import phonenumbers
from firebase_admin import auth
from firebase_admin import credentials

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

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
    workout.Button()
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
        self.warrButton = Button(self, image=self.warrPose, command=WarriorPose, border=0)
        self.warrButton.place(x=39, y=184)

        self.dogPose = PhotoImage(file="images/downward_facing_dog.png")
        self.dogButton = Button(self, image=self.dogPose, command=DownwardFacingDog, border=0)
        self.dogButton.place(x=39, y=476)

        self.bicepCurl = PhotoImage(file="images/bicep_curl.png")
        self.bicepButton = Button(self, image=self.bicepCurl, command=BicepCurl, border=0)
        self.bicepButton.place(x=731, y=184)

        self.overheadPress = PhotoImage(file="images/overhead_press.png")
        self.overheadButton = Button(self, image=self.overheadPress, command=OverheadPress, border=0, bg=None)
        self.overheadButton.place(x=731, y=476)


def calculate_angle(a, b, c):
    # Width 640 Height 480  -- Default, because changing the size lowers the quality

    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


def BicepCurl():
    cap = cv2.VideoCapture(0)

    # Curl counter variables
    R_counter = 0
    L_counter = 0
    L_stage = "down"
    R_stage = "down"
    tip = "Start the exercise!"

    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates of left arm
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                # Get coordinates of right arm
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                # Calculate angle
                left_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
                right_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

                # Visualize angle
                cv2.putText(image, str(left_angle), tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, str(right_angle), tuple(np.multiply(right_elbow, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                # Console output

                print("Left angle: ", f'{left_angle:.2f}', " | ", "Right Angle: ", f'{right_angle:.2f}')

                # Curl counter logic
                if left_angle > 160:
                    L_stage = "down"
                if left_angle < 30 and L_stage == "down":
                    tip = "You got it! Now lower your arm back down and repeat the motion"
                    L_stage = "up"
                    L_counter += 1

                if right_angle > 160:
                    R_stage = "down"
                if right_angle < 30 and R_stage == "down":
                    tip = "You got it! Now lower your arm back down and repeat the motion"
                    R_stage = "up"
                    R_counter += 1

                if 160 > left_angle > 95 or 160 > right_angle > 95:
                    tip = "Squeeze the biceps to curl the barbell to less than 30 degrees"
                if 90 > left_angle > 40 or 90 > right_angle > 40:
                    tip = "Squeeze the biceps a little bit more"

                print("Left arms rep count: ", f'{L_counter:.0f}', " | ", "Right arms rep count: ", f'{R_counter:.0f}')

            except:
                pass

            # Render curl counter
            # Setup status box
            cv2.rectangle(image, (0, 0), (640, 35), (240, 240, 240), -1)

            # Rep data
            # Right Arm
            cv2.putText(image, "R-Arm's rep count:", (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(R_counter), (145, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Left Arm
            cv2.putText(image, "L-Arm's rep count:", (165, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1,
                        cv2.LINE_AA)
            cv2.putText(image, str(L_counter), (305, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Stage data
            cv2.putText(image, 'R-Stage:', (350, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, R_stage, (410, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            cv2.putText(image, 'L-Stage:', (450, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, L_stage, (510, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Tips
            cv2.putText(image, 'Tip:', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, tip, (42, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            bicepImage = cv2.imread('images/bicep_curl_big.png')
            numpy_horizontal_concat = np.concatenate((image, bicepImage), axis=1)

            cv2.imshow('Bicep curl counter..', numpy_horizontal_concat)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


def OverheadPress():
    cap = cv2.VideoCapture(0)

    # Curl counter variables
    counter = -1
    stage = "down"
    tip = "Start the exercise!"

    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates of left arm
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                # Get coordinates of right arm
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                # Calculate angle
                left_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
                right_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

                # Visualize angle
                cv2.putText(image, str(left_angle), tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, str(right_angle), tuple(np.multiply(right_elbow, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                # Console output
                print("Left angle: ", f'{left_angle:.2f}', " | ", "Right Angle: ", f'{right_angle:.2f}')

                # Curl counter logic
                if left_angle < 45 and right_angle < 45:
                    stage = "down"
                    tip = "Press the bar directly over your head"

                if left_angle > 150 and right_angle > 150 and stage == "down":
                    stage = "up"
                    tip = "Slowly lower the bar in the exact same way you raised it"
                    counter += 1
                    print(counter)

            except:
                pass

            # Render curl counter
            # Setup status box
            cv2.rectangle(image, (0, 0), (640, 35), (240, 240, 240), -1)

            # Rep data
            cv2.putText(image, 'Rep count:', (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (105, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Stage data
            cv2.putText(image, 'Stage:', (150, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, (215, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Tips
            cv2.putText(image, 'Tip:', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, tip, (42, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            overheadImage = cv2.imread('images/overhead_press_big.png')
            numpy_horizontal_concat = np.concatenate((image, overheadImage), axis=1)

            cv2.imshow('Overhead press counter..', numpy_horizontal_concat)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


def WarriorPose():
    cap = cv2.VideoCapture(0)

    # Warrior Pose counter variables
    stage = "Not a warrior pose"
    tip = "Start the exercise!"
    l_arm, r_arm = "-", "-"
    l_leg, r_leg = "-", "-"

    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates of right leg
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                # Get coordinates of left leg
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                # Get coordinates of right arm
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                # Get coordinates of left arm
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                # Calculate angle
                right_leg_angle = calculate_angle(right_hip, right_knee, right_ankle)
                left_leg_angle = calculate_angle(left_hip, left_knee, left_ankle)

                right_arm_angle = calculate_angle(right_hip, right_shoulder, right_wrist)
                left_arm_angle = calculate_angle(left_hip, left_shoulder, left_wrist)

                # Visualize angle
                cv2.putText(image, str(left_leg_angle), tuple(np.multiply(left_knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, str(right_leg_angle), tuple(np.multiply(right_knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, str(right_arm_angle), tuple(np.multiply(right_shoulder, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, str(left_arm_angle), tuple(np.multiply(left_shoulder, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                # Console output
                print("Left leg: ", f'{left_leg_angle:.2f}', " | ", "Right leg: ", f'{right_leg_angle:.2f}', " | ",
                      "Left arm: ", f'{left_arm_angle:.2f}', " | ", "Right arm: ", f'{right_arm_angle:.2f}')

                # RIGHT LEG = Deg < 110 and Deg > 70
                # LEFT  LEG = Deg < 170 and Deg > 140
                # RIGHT ARM = Deg < 190 and Deg > 160
                # LEFT  ARM = Deg < 190 and Deg > 160

                if 110 > left_leg_angle > 70:
                    l_leg = "+"
                else:
                    l_leg = "-"
                if 170 > right_leg_angle > 140:
                    r_leg = "+"
                else:
                    r_leg = "-"
                if 190 > right_arm_angle > 160:
                    r_arm = "+"
                else:
                    r_arm = "-"
                if 190 > left_arm_angle > 160:
                    l_arm = "+"
                else:
                    l_arm = "-"

                if r_arm == "+" and l_arm == "+":
                    tip = "Arms are in place, focus on the legs"
                else:
                    tip = ""
                if r_leg == "+" and l_leg == "+":
                    tip = "Legs are in place, focus on the arms"

                if l_leg == "+" and r_leg == "+" and l_arm == "+" and r_arm == "+":
                    stage = "Warrior pose achieved"
                    tip = "Hold the pose"
                    print("ACHIEVED")
                else:
                    stage = "You have not achieved the warrior pose"

            except:
                pass

            # Setup status box
            cv2.rectangle(image, (0, 0), (640, 35), (240, 240, 240), -1)

            # Stage data
            cv2.putText(image, 'Stage:', (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, (55, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Left leg data
            cv2.putText(image, 'L Leg:', (315, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, l_leg, (360, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Right leg data
            cv2.putText(image, 'R Leg:', (380, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, r_leg, (425, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Left arm data
            cv2.putText(image, 'L Arm:', (445, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, l_arm, (490, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Right arm data
            cv2.putText(image, 'R Arm:', (510, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, r_arm, (555, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Tips
            cv2.putText(image, 'Tip:', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, tip, (42, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            warrImage = cv2.imread('images/warrior_pose_big.png')
            numpy_horizontal_concat = np.concatenate((image, warrImage), axis=1)

            cv2.imshow('Yoga - Warrior pose..', numpy_horizontal_concat)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


def DownwardFacingDog():
    cap = cv2.VideoCapture(0)

    # Warrior Pose counter variables
    stage = "Not the downward facing dog pose"
    tip = "Start the exercise!"
    l_arm, r_arm = "-", "-"
    l_leg, r_leg = "-", "-"

    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates of right arm
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                # Get coordinates of right leg
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                # Calculate angles
                right_leg_angle = calculate_angle(right_hip, right_knee, right_ankle)
                right_arm_angle = calculate_angle(right_wrist, right_shoulder, right_hip)

                # Visualize angles
                cv2.putText(image, str(right_leg_angle), tuple(np.multiply(right_knee, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                cv2.putText(image, str(right_arm_angle), tuple(np.multiply(right_shoulder, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                # Console output
                print("Right leg: ", f'{right_leg_angle:.2f}', " | ", "Right arm: ", f'{right_arm_angle:.2f}')

                # LEG = Deg < 175 and Deg > 165
                # ARM = Deg < 180 and Deg > 150

                if 180 > right_arm_angle > 150:
                    r_arm = "+"
                    tip = "Arms look good, focus on the legs"
                else:
                    r_arm = "-"

                if 180 > right_leg_angle > 165:
                    r_leg = "+"
                    tip = "Legs look good, focus on the arms"
                else:
                    r_leg = "-"

                if r_arm == "-" and r_leg == "-":
                    tip = "Nor arms or legs are in place"

                if r_arm == "+" and r_leg == "+":
                    stage = "Downward facing dog pose achieved"
                    tip = "Hold the pose"
                    print("ACHIEVED")
                else:
                    stage = "You have not achieved the downward facing dog pose"

            except:
                pass

            # Setup status box
            cv2.rectangle(image, (0, 0), (640, 35), (240, 240, 240), -1)

            # Stage data
            cv2.putText(image, 'Stage:', (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, (55, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Left arm data
            cv2.putText(image, 'R Leg:', (445, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, r_leg, (490, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Right arm data
            cv2.putText(image, 'R Arm:', (510, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, r_arm, (555, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Tips
            cv2.putText(image, 'Tip:', (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, tip, (42, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            downwardImage = cv2.imread('images/downward_facing_dog_big.png')
            numpy_horizontal_concat = np.concatenate((image, downwardImage), axis=1)

            cv2.imshow('Yoga - Downward facing dog..', numpy_horizontal_concat)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    Login = Login()
    Login.Label()
    Login.Entry()
    Login.Button()
    Login.mainloop()