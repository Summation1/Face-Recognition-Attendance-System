from tkinter import *
from tkinter import ttk
from tkinter import END
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import threading


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 35, "bold"),
            bg="sky blue",
            fg="green",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ======left image======
        img_bottom_path = r"college_images\face_detector1.jpg"
        if os.path.exists(img_bottom_path):
            img_bottom = Image.open(img_bottom_path)
            img_bottom = img_bottom.resize((650, 730), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl3 = Label(self.root, image=self.photoimg_bottom)
            f_lbl3.place(x=0, y=55, width=650, height=730)
        else:
            print(f"Image not found: {img_bottom_path}")

        # ======right image======
        img_top_path = r"college_images\p1.jpg"
        if os.path.exists(img_top_path):
            img_top = Image.open(img_top_path)
            img_top = img_top.resize((950, 730), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl3 = Label(self.root, image=self.photoimg_top)
            f_lbl3.place(x=650, y=55, width=950, height=730)
        else:
            print(f"Image not found: {img_top_path}")

        # Button
        b1 = Button(
            f_lbl3,
            text="Face Recognition",
            command=self.start_face_recog_thread,
            cursor="hand2",
            bg="blue",
            fg="white",
            font=("times new roman", 18, "bold"),
        )
        b1.place(x=370, y=650, width=200, height=40)

    def start_face_recog_thread(self):
        threading.Thread(target=self.face_recog, daemon=True).start()

    # ======= Attendance==============

    def mark_attendance(
        self,
        Name,
        Student_ID,
        Roll_No,
        Course,
        Section,
        Year,
        Semester,
        Department,
        Gender,
    ):
        with open("Attendance.csv", "r+", newline="\n") as f:  # Open in read mode
            myDataList = f.readlines()
            name_List = []
            for line in myDataList:
                entry = line.split((","))
                name_List.append(entry[0])
            if (
                (Roll_No not in name_List)
                and (Student_ID not in name_List)
                and (Name not in name_List)
                and (Course not in name_List)
                and (Section not in name_List)
            ):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(
                    f"{Name},{Student_ID},{Roll_No},{Course},{Department},{Year},{Semester},{Section},{Gender},{dtString},{d1},Present\n"
                )

    # ========== Face Recognition=============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors
            )

            coord = []
            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Shivanshu@123",
                    database="Face_Recogniser",
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "SELECT Name, Roll_No , Section, Course ,Student_ID,Year,Department,Semester,Gender FROM student WHERE Roll_No=%s",
                    (id,),
                )
                result = my_cursor.fetchone()
                conn.close()

                if result:
                    (
                        Name,
                        Roll_No,
                        Section,
                        Course,
                        Student_ID,
                        Year,
                        Department,
                        Semester,
                        Gender,
                    ) = result
                else:
                    (
                        Name,
                        Roll_No,
                        Section,
                        Course,
                        Student_ID,
                        Year,
                        Department,
                        Semester,
                        Gender,
                    ) = (
                        "N/A",
                        "N/A",
                        "N/A",
                        "N/A",
                        "N/A",
                        "N/A",
                        "N/A",
                        "N/A",
                        "N/A",
                    )

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"Name: {Name}",
                        (x, y - 120),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Student_ID: {Student_ID}",
                        (x, y - 95),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255),
                        3,
                    )

                    cv2.putText(
                        img,
                        f"Section: {Section}",
                        (x, y - 70),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Course: {Course}",
                        (x, y - 45),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Roll_No: {Roll_No}",
                        (x, y - 20),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255),
                        3,
                    )

                    self.mark_attendance(
                        Name,
                        Student_ID,
                        Roll_No,
                        Course,
                        Section,
                        Year,
                        Semester,
                        Department,
                        Gender,
                    )
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 45),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255),
                        3,
                    )

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
