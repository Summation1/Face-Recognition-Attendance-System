from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(
            self.root,
            text="DEVELOPER",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1540, height=45)

        img_top_path = r"college_images\dev.jpg"
        if os.path.exists(img_top_path):
            img_top = Image.open(img_top_path)
            img_top = img_top.resize((1530, 720), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl3 = Label(self.root, image=self.photoimg_top)
            f_lbl3.place(x=0, y=55, width=1530, height=720)
        else:
            print(f"Image not found: {img_top_path}")

        # ====Frame====
        main_frame = Frame(f_lbl3, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_topp_path = r"college_images\dev2.jpg"
        if os.path.exists(img_topp_path):
            img_topp = Image.open(img_topp_path)
            img_topp = img_topp.resize((200, 200), Image.LANCZOS)
            self.photoimg_topp = ImageTk.PhotoImage(img_topp)

            f_lbl3 = Label(main_frame, image=self.photoimg_topp)
            f_lbl3.place(x=300, y=0, width=200, height=200)
        else:
            print(f"Image not found: {img_topp_path}")

        # developer info
        dev_label = Label(
            main_frame,
            text="Hello ! my name is Shivanshu",
            font=("times new roman", 15, "bold"),
            bg="white",
        )

        dev_label.place(x=0, y=5)

        dev2_label = Label(
            main_frame,
            text="I am a full stack developer",
            font=("times new roman", 15, "bold"),
            bg="white",
        )

        dev2_label.place(x=0, y=40)

        dev3_label = Label(
            main_frame,
            text="Contact:9149163568",
            font=("times new roman", 20, "bold"),
            bg="white",
        )

        dev3_label.place(x=0, y=80)

        dev4_label = Label(
            main_frame,
            text=" Mail ID:-",
            font=("times new roman", 20, "bold"),
            bg="white",
        )

        dev4_label.place(x=0, y=120)

        dev5_label = Label(
            main_frame,
            text="shivanshuagarwal960@gmail.com",
            font=("times new roman", 15, "bold"),
            bg="white",
        )

        dev5_label.place(x=0, y=160)

        img_to_path = r"college_images\developer.jpg"
        if os.path.exists(img_topp_path):
            img_to = Image.open(img_to_path)
            img_to = img_to.resize((500, 400), Image.LANCZOS)
            self.photoimg_to = ImageTk.PhotoImage(img_to)

            f_lbl3 = Label(main_frame, image=self.photoimg_to)
            f_lbl3.place(x=0, y=200, width=500, height=400)
        else:
            print(f"Image not found: {img_to_path}")


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
