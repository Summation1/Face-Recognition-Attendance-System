from tkinter import *
from tkinter import ttk
from tkinter import END
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("times new roman", 35, "bold"),
            bg="blue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1540, height=45)

        img_top_path = r"college_images\rec.png"
        if os.path.exists(img_top_path):
            img_top = Image.open(img_top_path)
            img_top = img_top.resize((1530, 325), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl3 = Label(self.root, image=self.photoimg_top)
            f_lbl3.place(x=0, y=55, width=1530, height=330)
        else:
            print(f"Image not found: {img_top_path}")

        # ===Button======
        b1 = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_classifier,
            cursor="hand2",
            bg="blue",
            fg="white",
            font=("times new roman", 30, "bold"),
        )
        b1.place(x=0, y=380, width=1530, height=60)

        img_bottom_path = r"college_images\photos.jpg"
        if os.path.exists(img_bottom_path):
            img_bottom = Image.open(img_bottom_path)
            img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl3 = Label(self.root, image=self.photoimg_bottom)
            f_lbl3.place(x=0, y=440, width=1530, height=330)
        else:
            print(f"Image not found: {img_bottom_path}")

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # Gray Scale image
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])

            # "C:\Users\shiva\Desktop\face recognition project\data\user.3.1.jpg"
            # index [0]                                           index[1]
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ============Train the classifier And save====
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
