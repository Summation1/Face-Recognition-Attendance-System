from tkinter import *
from tkinter import ttk
from tkinter import END
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =========variables=========
        self.var_course = StringVar()
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
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
        img2_path = r"college_images\bg2.jpg"
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
            img3 = img3.resize((550, 130), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_lbl3 = Label(self.root, image=self.photoimg3)
            f_lbl3.place(x=1000, y=0, width=550, height=130)
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
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1540, height=45)

        main_frame = Frame(BG_lbl, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1522, height=645)

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=760, height=625)

        img_left_path = r"college_images\student1.jpg"
        if os.path.exists(img_left_path):
            img_left = Image.open(img_left_path)
            img_left = img_left.resize((750, 130), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl3 = Label(Left_frame, image=self.photoimg_left)
            f_lbl3.place(x=5, y=0, width=750, height=130)
        else:
            print(f"Image not found: {img_left_path}")

        # Current Course
        Current_Course_frame = LabelFrame(
            Left_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Current Course Information",
            font=("times new roman", 12, "bold"),
        )
        Current_Course_frame.place(x=3, y=135, width=750, height=120)
        # course
        course_label = Label(
            Current_Course_frame,
            text="Course",
            font=("times new roman", 12, "bold"),
            bg="white",
        )

        course_label.grid(row=0, column=0, padx=10, sticky=W)
        course_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_course,
            font=("times new roman", 12, "bold"),
            width=17,
            state="read only",
        )
        course_combo["values"] = ("Select Course", "B.Tech", "BCA", "BSc")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # department
        dep_label = Label(
            Current_Course_frame,
            text="Department",
            font=("times new roman", 12, "bold"),
            bg="white",
        )

        dep_label.grid(row=0, column=2, padx=10, sticky=W)
        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_department,
            font=("times new roman", 12, "bold"),
            width=17,
            state="read only",
        )
        dep_combo["values"] = (
            "Select Department",
            "CSE",
            "MECHANICAL",
            "CIVIL",
            "SPECIALIZATION",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(
            Current_Course_frame,
            text="Current Year",
            font=("times new roman", 12, "bold"),
            bg="white",
        )

        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_year,
            font=("times new roman", 12, "bold"),
            width=17,
            state="read only",
        )
        year_combo["values"] = (
            "Select Year",
            "First year",
            "Second year",
            "Third year",
            "Fourth year",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        # semester
        semester_label = Label(
            Current_Course_frame,
            text=" Current Semester",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_sem,
            font=("times new roman", 12, "bold"),
            width=17,
            state="read only",
        )
        semester_combo["values"] = (
            "Select Semester",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
        )
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # Student Information
        class_student_frame = LabelFrame(
            Left_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Class Student  Information",
            font=("times new roman", 12, "bold"),
        )
        class_student_frame.place(x=3, y=260, width=750, height=338)

        # Student id

        student_id_label = Label(
            class_student_frame,
            text="Student ID",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        student_id_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_id,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        # Student Name
        student_name_label = Label(
            class_student_frame,
            text="Student Name",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        student_name_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_name,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        class_division_label = Label(
            class_student_frame,
            text="Section",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        class_division_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        class_division_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_div,
            font=("times new roman", 12, "bold"),
            width=20,
        )
        class_division_combo["values"] = (
            "Select Section",
            "A1",
            "A2",
            "B1",
            "B2",
            "C1",
            "C2",
            "D1",
            "D2",
        )
        class_division_combo.current(0)
        class_division_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        # Roll no

        student_roll_label = Label(
            class_student_frame,
            text="Roll No.",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_roll_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        student_roll_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        # Gender
        student_gender_label = Label(
            class_student_frame,
            text="Gender",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        student_gender_combo = ttk.Combobox(
            class_student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 12, "bold"),
            width=20,
        )
        student_gender_combo["values"] = (
            "Select Gender",
            "Male",
            "Female",
            "Other",
        )
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        # Dob
        student_dob_label = Label(
            class_student_frame,
            text="Date Of Birth",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_dob_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        student_dob_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        # Email
        student_email_label = Label(
            class_student_frame,
            text="Email",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        student_email_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        # Phone No
        student_phone_label = Label(
            class_student_frame,
            text="Phone No.",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_phone_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        student_phone_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        # Address
        student_address_label = Label(
            class_student_frame,
            text="Address.",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        student_address_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        # Teacher Name
        student_teacher_label = Label(
            class_student_frame,
            text="Class Coordinator Name",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_teacher_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)
        student_teacher_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        student_teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        # Radio Buttons
        self.var_radio1 = StringVar()

        radio_b1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes",
        )
        radio_b1.grid(row=5, column=0)

        radio_b2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="No Photo Sample",
            value="No",
        )
        radio_b2.grid(row=5, column=1)

        # buttons Frame

        btn_frame = Frame(class_student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=240, width=745, height=36)

        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=19,
            height=1,
            cursor="hand2",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="update",
            font=("times new roman", 12, "bold"),
            command=self.update_data,
            bg="blue",
            fg="white",
            width=20,
            height=1,
            cursor="hand2",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=19,
            height=1,
            cursor="hand2",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=20,
            height=1,
            cursor="hand2",
        )
        reset_btn.grid(row=0, column=3)

        btn2_frame = Frame(class_student_frame, bd=2, bg="white", relief=RIDGE)
        btn2_frame.place(x=0, y=276, width=745, height=36)

        photo_sample_btn = Button(
            btn2_frame,
            text="Take a Photo",
            command=self.generate_dataset,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=83,
            height=1,
            cursor="hand2",
            anchor=CENTER,
        )
        photo_sample_btn.grid(row=0, column=0)

        """photo_update_btn = Button(
            btn2_frame,
            text="Update Photo Sample",
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=42,
            height=1,
            cursor="hand2",
        )
        photo_update_btn.grid(row=0, column=1)"""

        # Right label frame
        Right_frame = LabelFrame(
            main_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=780, y=10, width=730, height=625)
        img_right_path = r"college_images\student1.jpg"
        if os.path.exists(img_right_path):
            img_right = Image.open(img_right_path)
            img_right = img_right.resize((700, 130), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)

            f_lbl3 = Label(Right_frame, image=self.photoimg_right)
            f_lbl3.place(x=5, y=0, width=700, height=130)
        else:
            print(f"Image not found: {img_right_path}")
        # =======SEarch System============
        Search_frame = LabelFrame(
            Right_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=3, y=135, width=720, height=70)

        Search_label = Label(
            Search_frame,
            text="Search By:",
            font=("times new roman", 12, "bold"),
            bg="red",
            fg="white",
        )
        Search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # search
        self.var_com_search = StringVar()
        Search_combo = ttk.Combobox(
            Search_frame,
            textvariable=self.var_com_search,
            font=("times new roman", 12, "bold"),
            width=12,
            state="read only",
        )
        Search_combo["values"] = (
            "Select Option",
            "Name",
            "Student_ID",
        )
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        self.var_search_entry = StringVar()
        Search_entry = ttk.Entry(
            Search_frame,
            textvariable=self.var_search_entry,
            width=20,
            font=("times new roman", 12, "bold"),
        )
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Search_btn = Button(
            Search_frame,
            text="Search",
            command=self.search_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=15,
            height=1,
            cursor="hand2",
        )
        Search_btn.grid(row=0, column=3, padx=4)

        ShowAll_btn = Button(
            Search_frame,
            text="Show All",
            command=self.fetch_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=15,
            height=1,
            cursor="hand2",
        )
        ShowAll_btn.grid(row=0, column=4, padx=4)

        # =========Table Frame===========

        table_frame = LabelFrame(
            Right_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
        )
        table_frame.place(x=3, y=210, width=720, height=390)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "Course",
                "Department",
                "Year",
                "Semester",
                "Student_Id",
                "Name",
                "Section",
                "Roll_No",
                "Gender",
                "DOB",
                "Email",
                "Phone no.",
                "Address",
                "CC",
                "Photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            show="headings",
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student_Id", text="Student_Id")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Roll_No", text="Roll_No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone no.", text="Phone no.")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("CC", text="CC")
        self.student_table.heading("Photo", text="Photo")
        self.student_table.column("Course", width=100)
        self.student_table.column("Department", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Student_Id", width=100)
        self.student_table.column("Name", width=200)
        self.student_table.column("Section", width=100)
        self.student_table.column("Roll_No", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=300)
        self.student_table.column("Phone no.", width=100)
        self.student_table.column("Address", width=200)
        self.student_table.column("CC", width=100)
        self.student_table.column("Photo", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =========function Declaration=========

    def add_data(self):
        if (
            self.var_department.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get == ""
            or self.var_course.get() == "Select Course"
        ):
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Shivanshu@123",
                    database="Face_Recogniser",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_course.get(),
                        self.var_department.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added successfully ",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Shivanshu@123",
            database="Face_Recogniser",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ================== get cursor==========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0])
        self.var_department.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # -----Update Function--------
    def update_data(self):
        if (
            self.var_department.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
            or self.var_course.get() == "Select Course"
        ):
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student details",
                    parent=self.root,
                )
                if update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Shivanshu@123",
                        database="Face_Recogniser",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Course=%s, `Department`=%s, `Year`=%s, `Semester`=%s, `Name`=%s, `Section`=%s, `Roll_No`=%s, `Gender`=%s, `DOB`=%s, `Email`=%s, `Phone_No.`=%s, `Address`=%s, `Teacher`=%s, `Photo`=%s WHERE `Student_ID`=%s",
                        (
                            self.var_course.get(),
                            self.var_department.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_id.get(),
                        ),
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Success",
                        "Student Details Successfully updated",
                        parent=self.root,
                    )

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ====== Delete Function==========

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student detail ?",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Shivanshu@123",
                        database="Face_Recogniser",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_ID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ======Reset button===
    def reset_data(self):
        self.var_course.set("Select Course")
        self.var_department.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ===== search dat=====

    def search_data(self):
        if not self.var_com_search.get() or not self.var_search_entry.get():
            messagebox.showerror("Error", "Please select an option")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Shivanshu@123",
                database="Face_Recogniser",
            )
            my_cursor = conn.cursor()

            column_name = self.var_com_search.get()
            search_value = f"%{self.var_search_entry.get()}%"

            query = f"SELECT * FROM student WHERE {column_name} LIKE %s"

            my_cursor.execute(query, (search_value,))
            data = my_cursor.fetchall()

            if data:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
                conn.commit()
            else:
                messagebox.showinfo("No Results", "No matching records found")

            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)

    # =================== Generate data set or Take Photo Sample
    def generate_dataset(self):
        if (
            self.var_department.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
            or self.var_course.get() == "Select Course"
        ):
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Shivanshu@123",
                    database="Face_Recogniser",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "UPDATE student SET Course=%s, `Department`=%s, `Year`=%s, `Semester`=%s, `Name`=%s, `Section`=%s, `Roll_No`=%s, `Gender`=%s, `DOB`=%s, `Email`=%s, `Phone_No.`=%s, `Address`=%s, `Teacher`=%s, `Photo`=%s WHERE `Student_ID`=%s",
                    (
                        self.var_course.get(),
                        self.var_department.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ========== Load predefined data on face from opencv====

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # Minimum Neighbor=5

                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped
                    return None  # Ensure it returns None if no face is found

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if ret:  # Check if the frame is read correctly
                        face = face_cropped(my_frame)
                        if face is not None:
                            img_id += 1  # Incrementing img_id
                            face = cv2.resize(face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = (
                                "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            )
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(
                                face,
                                str(img_id),
                                (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                2,
                                (0, 255, 0),
                                2,
                            )
                            cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
