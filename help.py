from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(
            self.root,
            text="Help Desk",
            font=("times new roman", 35, "bold"),
            fg="brown",
            bg="yellow",
        )
        title_lbl.place(x=0, y=0, width=1540, height=45)

        img_top_path = r"college_images\dev3.jpeg"
        if os.path.exists(img_top_path):
            img_top = Image.open(img_top_path)
            img_top = img_top.resize((1530, 720), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl3 = Label(self.root, image=self.photoimg_top)
            f_lbl3.place(x=0, y=55, width=1530, height=720)
        else:
            print(f"Image not found: {img_top_path}")

        title_lbl = Label(
            self.root,
            text="Email:shivanshuagarwal960@gmail.com",
            font=("times new roman", 25, "bold"),
            fg="brown",
            bg="white",
        )
        title_lbl.place(x=440, y=300, width=630, height=50)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
