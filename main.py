from time import strftime
from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk, ImageEnhance
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os


class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img1_path = r"college_images\gehu2.jpg"
        if os.path.exists(img1_path):
            img1 = Image.open(img1_path)
            img1 = img1.resize((500, 130), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=0, y=0, width=500, height=130)
        else:
            print(f"Image not found: {img1_path}")

        # Second Image
        img2_path = r"college_images\rec.png"
        if os.path.exists(img2_path):
            img2 = Image.open(img2_path)
            img2 = img2.resize((500, 130), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=500, y=0, width=500, height=130)
        else:
            print(f"Image not found: {img2_path}")

        # Third Image
        img3_path = r"college_images\gehu.jpg"
        if os.path.exists(img3_path):
            img3 = Image.open(img3_path)
            img3 = img3.resize((1550, 130), Image.LANCZOS)
            # Enhance the image
            enhancer = ImageEnhance.Sharpness(img3)
            img3 = enhancer.enhance(2.0)  # Increase sharpness
            enhancer = ImageEnhance.Contrast(img3)
            img3 = enhancer.enhance(1.5)  # Increase contrast
            enhancer = ImageEnhance.Brightness(img3)
            img3 = enhancer.enhance(1.2)  # Increase brightness
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_lbl3 = Label(self.root, image=self.photoimg3)
            f_lbl3.place(x=0, y=0, width=1550, height=130)
        else:
            print(f"Image not found: {img3_path}")
        # Background Image
        img4_path = r"college_images\face.png"
        if os.path.exists(img4_path):
            img4 = Image.open(img4_path)
            img4 = img4.resize((1550, 710), Image.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)
            BG_lbl = Label(self.root, image=self.photoimg4)
            BG_lbl.place(x=0, y=130, width=1550, height=710)
        else:
            print(f"Image not found: {img4_path}")

        # Title Label
        title_lbl = Label(
            BG_lbl,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # time window ====

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(
            title_lbl,
            font=("times new roman", 14, "bold"),
            background="white",
            foreground="brown",
        )
        lbl.place(x=1400, y=(-15), width=110, height=50)

        time()

        # Student button
        img5_path = r"college_images\student.jpg"
        if os.path.exists(img5_path):
            img5 = Image.open(img5_path)
            img5 = img5.resize((220, 220), Image.LANCZOS)
            self.photoimg5 = ImageTk.PhotoImage(img5)

            b1 = Button(
                BG_lbl,
                image=self.photoimg5,
                command=self.student_details,
                cursor="hand2",
            )
            b1.place(x=200, y=100, width=220, height=200)

            b1_label = Button(
                BG_lbl,
                text="Student Details",
                command=self.student_details,
                cursor="hand2",
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b1_label.place(x=200, y=300, width=220, height=40)
        else:
            print(f"Image not found: {img5_path}")

        # Face Detector button
        img6_path = r"college_images\new2.png"
        if os.path.exists(img6_path):
            img6 = Image.open(img6_path)
            img6 = img6.resize((220, 220), Image.LANCZOS)
            self.photoimg6 = ImageTk.PhotoImage(img6)

            b2 = Button(
                BG_lbl, image=self.photoimg6, command=self.face_data, cursor="hand2"
            )
            b2.place(x=500, y=100, width=220, height=200)

            b2_label = Button(
                BG_lbl,
                text="Face Detector",
                command=self.face_data,
                cursor="hand2",
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b2_label.place(x=500, y=300, width=220, height=40)
        else:
            print(f"Image not found: {img6_path}")

        # Attendance button
        img7_path = r"college_images\attendance.jpeg"
        if os.path.exists(img7_path):
            img7 = Image.open(img7_path)
            img7 = img7.resize((220, 220), Image.LANCZOS)
            self.photoimg7 = ImageTk.PhotoImage(img7)

            b3 = Button(
                BG_lbl,
                image=self.photoimg7,
                cursor="hand2",
                command=self.attendance_data,
            )
            b3.place(x=800, y=100, width=220, height=200)

            b3_label = Button(
                BG_lbl,
                text="ATTENDANCE",
                command=self.attendance_data,
                cursor="hand2",
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b3_label.place(x=800, y=300, width=220, height=40)
        else:
            print(f"Image not found: {img7_path}")

        # Help button
        img8_path = r"college_images\helpdesk.jpg"
        if os.path.exists(img8_path):
            img8 = Image.open(img8_path)
            img8 = img8.resize((220, 220), Image.LANCZOS)
            self.photoimg8 = ImageTk.PhotoImage(img8)

            b4 = Button(
                BG_lbl, image=self.photoimg8, cursor="hand2", command=self.help_data
            )
            b4.place(x=1100, y=100, width=220, height=200)

            b4_label = Button(
                BG_lbl,
                text="HELP & SUPPORT",
                cursor="hand2",
                command=self.help_data,
                font=("times new roman", 15, "bold"),
                bg="black",
                fg="blue",
            )
            b4_label.place(x=1100, y=300, width=220, height=40)
        else:
            print(f"Image not found: {img8_path}")

        # Train Data button
        img9_path = r"college_images\face_det.jpg"
        if os.path.exists(img9_path):
            img9 = Image.open(img9_path)
            img9 = img9.resize((220, 220), Image.LANCZOS)
            self.photoimg9 = ImageTk.PhotoImage(img9)

            b5 = Button(
                BG_lbl, image=self.photoimg9, command=self.train_data, cursor="hand2"
            )
            b5.place(x=200, y=400, width=220, height=200)

            b5_label = Button(
                BG_lbl,
                text="TRAIN DATA",
                command=self.train_data,
                cursor="hand2",
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b5_label.place(x=200, y=600, width=220, height=40)
        else:
            print(f"Image not found: {img9_path}")

        # Photos button
        img10_path = r"college_images\photos.jpg"
        if os.path.exists(img10_path):
            img10 = Image.open(img10_path)
            img10 = img10.resize((220, 220), Image.LANCZOS)
            self.photoimg10 = ImageTk.PhotoImage(img10)

            b6 = Button(
                BG_lbl, image=self.photoimg10, cursor="hand2", command=self.open_img
            )
            b6.place(x=500, y=400, width=220, height=200)

            b6_label = Button(
                BG_lbl,
                text="PHOTOS",
                command=self.open_img,
                cursor="hand2",
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b6_label.place(x=500, y=600, width=220, height=40)
        else:
            print(f"Image not found: {img10_path}")

        # Developer button
        img11_path = r"college_images\bg1.jpg"
        if os.path.exists(img11_path):
            img11 = Image.open(img11_path)
            img11 = img11.resize((220, 220), Image.LANCZOS)
            self.photoimg11 = ImageTk.PhotoImage(img11)

            b7 = Button(
                BG_lbl,
                image=self.photoimg11,
                cursor="hand2",
                command=self.developer_data,
            )
            b7.place(x=800, y=400, width=220, height=200)

            b7_label = Button(
                BG_lbl,
                text="DEVELOPER",
                command=self.developer_data,
                cursor="hand2",
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b7_label.place(x=800, y=600, width=220, height=40)
        else:
            print(f"Image not found: {img11_path}")

        # Exit button
        img12_path = r"college_images\exit.jpg"
        if os.path.exists(img12_path):
            img12 = Image.open(img12_path)
            img12 = img12.resize((220, 220), Image.LANCZOS)
            self.photoimg12 = ImageTk.PhotoImage(img12)

            b8 = Button(
                BG_lbl, image=self.photoimg12, cursor="hand2", command=self.exit
            )
            b8.place(x=1100, y=400, width=220, height=200)

            b8_label = Button(
                BG_lbl,
                text="EXIT",
                cursor="hand2",
                command=self.exit,
                font=("times new roman", 20, "bold"),
                bg="black",
                fg="blue",
            )
            b8_label.place(x=1100, y=600, width=220, height=40)
        else:
            print(f"Image not found: {img12_path}")

    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure to exit the project?", parent=self.root
        )
        if self.exit > 0:
            self.root.destroy()
        else:
            return

        # =========function button

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()
