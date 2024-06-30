from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_recognition_System  # Import the main application class


def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.iconbitmap("Images/logo_PI6_icon.ico")
        self.root.geometry("1500x800+0+0")

        try:
            self.bg = ImageTk.PhotoImage(file="Images/asus-zenbook.jpg")
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image not found.")
            self.bg = None

        if self.bg:
            bg_lbl = Label(self.root, image=self.bg)
            bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open("Images/r.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(
            frame,
            text="Get Started",
            font=("times new roman", 20, "bold"),
            fg="white",
            bg="black",
        )
        get_str.place(x=95, y=100)

        # label for Username
        username = lbl = Label(
            frame,
            text="Username/Email",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="black",
        )
        username.place(x=70, y=155)

        self.textuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.textuser.place(x=40, y=185, width=270)

        # Label for Password
        password = lbl = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="black",
        )
        password.place(x=70, y=225)

        self.textpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.textpass.place(x=40, y=255, width=270)

        # ======== Icon Images ===================================
        img2 = Image.open("Images/r.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=325, width=25, height=25)

        img3 = Image.open("Images/lock.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        # Login button
        loginbtn = Button(
            frame,
            command=self.login,
            text="Login",
            font=("times new roman", 15, "bold"),
            bd=5,
            relief=RIDGE,
            bg="red",
            fg="white",
            activebackground="red",
            activeforeground="white",
        )
        loginbtn.place(x=110, y=305, width=90, height=40)

        # ============= Forget Password ==================
        forgotbtn = Button(
            frame,
            command=self.forgot_password_window,
            text="Forget Password",
            font=("times new roman", 12, "bold"),
            borderwidth=0,
            bg="black",
            fg="white",
            activebackground="black",
            activeforeground="white",
        )
        forgotbtn.place(
            x=15,
            y=350,
            width=160,
        )

        # ============= New User ==================
        newregbtn = Button(
            frame,
            command=self.register_window,
            text="Creat New Account",
            font=("times new roman", 12, "bold"),
            borderwidth=0,
            bg="black",
            fg="white",
            activebackground="black",
            activeforeground="white",
        )
        newregbtn.place(
            x=22,
            y=385,
            width=160,
        )

    # ======== function ==========
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window, self)

    def login(self):
        if self.textuser.get() == "" or self.textpass.get() == "":
            messagebox.showerror("Error", "All Field are Required")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shivanshu@123",
                database="face_recogniser",
            )
            reg_cursor = conn.cursor()
            reg_cursor.execute(
                "select * from register where email=%s and password=%s",
                (self.textuser.get(), self.textpass.get()),
            )

            row = reg_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password.")
            else:
                self.root.destroy()  # Close the login window
                self.open_main_window()  # Open the main application window

            conn.commit()
            conn.close()

    def open_main_window(self):
        main_app = Face_recognition_System(Tk())
        main_app.root.mainloop()

    # ======== Reset Password function ====================
    def reset_pass(self):
        if self.combo_securiy_Q.get() == "Select Your Security Questions":
            messagebox.showerror(
                "Error", "Please Select Your Security Questions.", parent=self.root2
            )
        elif self.txt_security.get() == "":
            messagebox.showwarning(
                "Warning", "Please Enter The Answer.", parent=self.root2
            )
        elif self.txt_newpass.get() == "":
            messagebox.showwarning(
                "Warning", "Please Enter The New Password.", parent=self.root2
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shivanshu@123",
                database="face_recogniser",
            )
            reg_cursor = conn.cursor()
            qury = "select * from register where email=%s and securityQ=%s and securityA=%s"
            value = (
                self.textuser.get(),
                self.combo_securiy_Q.get(),
                self.txt_security.get(),
            )
            reg_cursor.execute(qury, value)
            row = reg_cursor.fetchone()
            if row == None:
                messagebox.showwarning(
                    "Warning", "Please Enter The Correct Answer.", parent=self.root2
                )
            else:
                query = "update register set password=%s where email=%s"
                value = (self.txt_newpass.get(), self.textuser.get())
                reg_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info",
                    "Your Password has been reset Successfully, \n Please Login with New Password.",
                    parent=self.root2,
                )
                self.root2.destroy()

    # ============================= Forgot Password Windows =========================
    def forgot_password_window(self):
        if self.textuser.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the Email Address To Reset Password"
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shivanshu@123",
                database="face_recogniser",
            )
            reg_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.textuser.get(),)
            reg_cursor.execute(query, value)
            row = reg_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Please Enter The Valid Username/Email name."
                )
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.iconbitmap("Images/logo_PI6_icon.ico")
                self.root2.geometry("340x450+610+170")

                fglbl = Label(
                    self.root2,
                    text="Forget Password",
                    font=("times new roman", 18, "bold"),
                    bg="black",
                    fg="red",
                )
                fglbl.place(x=0, y=10, relwidth=1)

                securiy_Q = Label(
                    self.root2,
                    text="Select Security Questions",
                    font=("times new roman", 15, "bold"),
                    bg="black",
                    fg="white",
                )
                securiy_Q.place(x=50, y=80)

                self.combo_securiy_Q = ttk.Combobox(
                    self.root2,
                    font=("times new roman", 15, "bold"),
                    state="readonly",
                )
                self.combo_securiy_Q["values"] = (
                    "Select Your Security Questions",
                    "Your Birth Place",
                    "Your Girlfriend Name",
                    "Your Pet Name",
                )
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A = Label(
                    self.root2,
                    text="Security Answer",
                    font=("times new roman", 15, "bold"),
                    bg="black",
                    fg="white",
                )
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(
                    self.root2,
                    font=("times new roman", 15, "bold"),
                )
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(
                    self.root2,
                    text="New Password",
                    font=("times new roman", 15, "bold"),
                    bg="black",
                    fg="white",
                )
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(
                    self.root2,
                    font=("times new roman", 15, "bold"),
                )
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(
                    self.root2,
                    text="Reset",
                    command=self.reset_pass,
                    font=("times new roman", 15, "bold"),
                    bg="red",
                    fg="white",
                    activebackground="red",
                    activeforeground="white",
                )
                btn.place(x=100, y=290)

    def open_login_window(self):
        # Close the current register window
        self.root.destroy()

        # Open the login window
        login_window = Tk()
        login_app = LoginWindow(login_window)
        login_window.mainloop()


class Register:
    def __init__(self, root, login_window_instance):

        self.root = root
        self.login_window_instance = login_window_instance
        self.root.title("Register")
        self.root.iconbitmap("Images/logo_PI6_icon.ico")
        self.root.geometry("1500x800+0+0")

        try:
            self.bg = ImageTk.PhotoImage(file="Images/asus-zenbook.jpg")
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image not found.")
            self.bg = None

        if self.bg:
            bg_lbl = Label(self.root, image=self.bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = ImageTk.PhotoImage(file="Images/asus-zenbook.jpg")
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="black")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(
            frame,
            text="REGISTER HERE",
            font=("times new roman", 20, "bold"),
            fg="white",
            bg="black",
        )
        register_lbl.place(x=20, y=20)

        # =============== Label and entry ==========================
        fname = Label(
            frame,
            text="First Name",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        lname = Label(
            frame,
            text="Last Name",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(
            frame,
            text="Contact No",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(
            frame,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        security_Q = Label(
            frame,
            text="Select Security Question",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        security_Q.place(x=50, y=240)

        self.combo_securiy_Q = ttk.Combobox(
            frame, font=("times new roman", 15, "bold"), state="readonly"
        )
        self.combo_securiy_Q["values"] = (
            "Select",
            "Your Birth Place",
            "Your Girlfriend Name",
            "Your Pet Name",
        )
        self.combo_securiy_Q.place(x=50, y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A = Label(
            frame,
            text="Security Answer",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        pswd = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(
            frame,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            bg="black",
            fg="white",
        )
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame, font=("times new roman", 15, "bold"), show="*"
        )
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # =============== CheckButton ====================
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(
            frame,
            variable=self.var_check,
            text="I Agree The Terms & Condition",
            font=("times new roman", 12, "bold"),
            onvalue=1,
            offvalue=0,
            bg="black",
            fg="white",
            activebackground="black",
            activeforeground="white",
            selectcolor="green",
        )
        self.checkbtn.place(x=50, y=380)

        # ============== Button ===========================
        img = Image.open("Images/Register1.png")
        img = img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(
            frame,
            image=self.photoimage,
            command=self.register_data,
            borderwidth=0,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
        )
        b1.place(x=60, y=420, width=200)

        img1 = Image.open("Images/login.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(
            frame,
            image=self.photoimage1,
            command=self.login_window_instance.open_login_window,
            borderwidth=0,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
        )
        b2.place(x=380, y=420, width=200)

    # ============== function declaration =============
    def register_data(self):
        if (
            self.fname_entry.get() == ""
            or self.txt_email.get() == ""
            or self.combo_securiy_Q.get() == "Select"
        ):
            messagebox.showerror("Error", "All Fields Are Required")
        elif self.txt_pswd.get() != self.txt_confirm_pswd.get():
            messagebox.showerror("Error", "Password & Confirm Password Must Be Same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Condition")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shivanshu@123",
                database="face_recogniser",
            )
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.txt_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist, Please try another email"
                )
            else:
                my_cursor.execute(
                    "insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.fname_entry.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.combo_securiy_Q.get(),
                        self.txt_security.get(),
                        self.txt_pswd.get(),
                    ),
                )

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Success", "Registered successfully", parent=self.root
                )


if __name__ == "__main__":
    main()
