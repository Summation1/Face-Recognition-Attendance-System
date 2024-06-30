from tkinter import *
from tkinter import ttk
from tkinter import END
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog
import os


mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance  System")

        # ========variables======

        self.var_course = StringVar()
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()

        # first image
        img1_path = r"college_images\report.jpg"
        if os.path.exists(img1_path):
            img1 = Image.open(img1_path)
            img1 = img1.resize((750, 200), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=0, y=0, width=750, height=200)
        else:
            print(f"Image not found: {img1_path}")

        # Second Image
        img2_path = r"college_images\smart-attendance.jpg"
        if os.path.exists(img2_path):
            img2 = Image.open(img2_path)
            img2 = img2.resize((790, 200), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=750, y=0, width=790, height=200)
        else:
            print(f"Image not found: {img2_path}")

        # =======Background Image===

        img4_path = r"C:\Users\shiva\Desktop\face recognition project\college_images\employee_img2.jpg"
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
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="black",
        )
        title_lbl.place(x=0, y=0, width=1540, height=45)

        main_frame = Frame(BG_lbl, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1522, height=600)

        Left_frame = LabelFrame(
            main_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left_path = r"college_images\attendance.jpeg"
        if os.path.exists(img_left_path):
            img_left = Image.open(img_left_path)
            img_left = img_left.resize((720, 230), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            f_lbl3 = Label(Left_frame, image=self.photoimg_left)
            f_lbl3.place(x=5, y=0, width=720, height=230)
        else:
            print(f"Image not found: {img_left_path}")

        Left_inner_frame = LabelFrame(
            Left_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            font=("times new roman", 12, "bold"),
        )
        Left_inner_frame.place(x=5, y=235, width=715, height=320)

        # ========Labels and Entry=====

        Student__Id_label = Label(
            Left_inner_frame,
            text="Student_ ID",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Student__Id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Student__Id_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_id,
            font=("times new roman", 12, "bold"),
        )
        Student__Id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name

        name_label = Label(
            Left_inner_frame,
            text="Name",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_name,
            font=("times new roman", 12, "bold"),
        )
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll

        Roll_label = Label(
            Left_inner_frame,
            text="Roll No.",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Roll_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Roll_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_roll,
            font=("times new roman", 12, "bold"),
        )
        Roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Course

        course_label = Label(
            Left_inner_frame,
            text="Course",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        course_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        course_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_course,
            font=("times new roman", 12, "bold"),
        )
        course_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(
            Left_inner_frame,
            text="Department",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        department_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        department_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_department,
            font=("times new roman", 12, "bold"),
        )
        department_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # gender

        gender_label = Label(
            Left_inner_frame,
            text="Gender",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        gender_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_gender,
            font=("times new roman", 12, "bold"),
        )
        gender_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # year

        Year_label = Label(
            Left_inner_frame,
            text="Year",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        Year_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        Year_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_year,
            font=("times new roman", 12, "bold"),
        )
        Year_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # semester

        semester_label = Label(
            Left_inner_frame,
            text="Semester",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        semester_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        semester_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_sem,
            font=("times new roman", 12, "bold"),
        )
        semester_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # time

        date_label = Label(
            Left_inner_frame,
            text="Time",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        date_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_date,
            font=("times new roman", 12, "bold"),
        )
        date_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # date
        date_label = Label(
            Left_inner_frame,
            text="Date",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        date_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(
            Left_inner_frame,
            width=20,
            textvariable=self.var_time,
            font=("times new roman", 12, "bold"),
        )
        date_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # class division

        class_division_label = Label(
            Left_inner_frame,
            text="Section",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        class_division_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        class_division_combo = ttk.Combobox(
            Left_inner_frame,
            font=("times new roman", 12, "bold"),
            textvariable=self.var_div,
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
        class_division_combo.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Attendance Status

        attendance_status_label = Label(
            Left_inner_frame,
            text="Attendance Status",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        attendance_status_label.grid(row=5, column=2, padx=10, pady=10, sticky=W)
        attendance_status_combo = ttk.Combobox(
            Left_inner_frame,
            font=("times new roman", 12, "bold"),
            textvariable=self.var_status,
            width=20,
        )
        attendance_status_combo["values"] = (
            "Select Status",
            "Present",
            "Absent",
            "Leave",
        )
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=5, column=3, padx=10, pady=5, sticky=W)

        # Buttons

        btn_frame = Frame(Left_inner_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=250, width=745, height=36)

        save_btn = Button(
            btn_frame,
            text="Import csv",
            command=self.importCsv,
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
            text="Export csv",
            command=self.exportCsv,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=19,
            height=1,
            cursor="hand2",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            font=("times new roman", 12, "bold"),
            command=self.delete_data,
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
            width=18,
            height=1,
            cursor="hand2",
        )
        reset_btn.grid(row=0, column=3)

        Right_frame = LabelFrame(
            main_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=750, y=10, width=740, height=580)

        table_frame = LabelFrame(
            Right_frame,
            bg="white",
            bd=2,
            relief=RIDGE,
        )
        table_frame.place(x=3, y=5, width=730, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.Attendance_report_table = ttk.Treeview(
            table_frame,
            columns=(
                "Name",
                "Student_Id",
                "Roll_No",
                "Course",
                "Department",
                "Year",
                "Semester",
                "Section",
                "Gender",
                "Date",
                "Time",
                "Attendance_status",
            ),
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Attendance_report_table.xview)
        scroll_y.config(command=self.Attendance_report_table.yview)

        self.Attendance_report_table.heading("Course", text="Course")
        self.Attendance_report_table.heading("Department", text="Department")
        self.Attendance_report_table.heading("Year", text="Year")
        self.Attendance_report_table.heading("Semester", text="Semester")
        self.Attendance_report_table.heading("Student_Id", text="Student_Id")
        self.Attendance_report_table.heading("Name", text="Name")
        self.Attendance_report_table.heading("Section", text="Section")
        self.Attendance_report_table.heading("Roll_No", text="Roll_No")
        self.Attendance_report_table.heading("Gender", text="Gender")
        self.Attendance_report_table.heading("Date", text="Date")
        self.Attendance_report_table.heading("Time", text="Time")
        self.Attendance_report_table.heading(
            "Attendance_status", text="Attendance Status"
        )
        self.Attendance_report_table["show"] = "headings"
        self.Attendance_report_table.column("Course", width=100)
        self.Attendance_report_table.column("Department", width=100)
        self.Attendance_report_table.column("Year", width=100)
        self.Attendance_report_table.column("Semester", width=100)
        self.Attendance_report_table.column("Student_Id", width=100)
        self.Attendance_report_table.column("Name", width=100)
        self.Attendance_report_table.column("Section", width=100)
        self.Attendance_report_table.column("Roll_No", width=100)
        self.Attendance_report_table.column("Gender", width=100)
        self.Attendance_report_table.column("Date", width=100)
        self.Attendance_report_table.column("Time", width=100)
        self.Attendance_report_table.column("Attendance_status", width=150)
        self.Attendance_report_table.pack(fill=BOTH, expand=1)
        self.Attendance_report_table.bind("<ButtonRelease>", self.get_cursor)

    # ==============================fetch data=============
    def fetchData(self, rows):
        self.Attendance_report_table.delete(
            *self.Attendance_report_table.get_children()
        )
        for i in rows:
            self.Attendance_report_table.insert("", END, values=i)

    # =====import csv======
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root,
        )
        if fln:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        else:
            messagebox.showinfo(
                "No File Selected", "No file selected.", parent=self.root
            )

    # ======= export csv====
    def exportCsv(self):
        try:
            items = self.Attendance_report_table.get_children()
            if not items:
                messagebox.showerror(
                    "No Data", "No Data Found to export ", parent=self.root
                )
                return

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root,
            )
            if not fln:
                return  # User cancelled the save dialog

            if not fln.endswith(".csv"):
                fln += ".csv"

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for item in items:
                    row = self.Attendance_report_table.item(item)["values"]
                    exp_write.writerow(row)

            messagebox.showinfo(
                "Data Export",
                "Your Data Exported to " + os.path.basename(fln) + " successfully",
                parent=self.root,
            )
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        try:
            cursor_row = self.Attendance_report_table.focus()
            content = self.Attendance_report_table.item(cursor_row)
            rows = content["values"]

            if len(rows) < 12:
                raise ValueError("Selected row does not contain enough data")

            self.var_name.set(rows[0])
            self.var_id.set(rows[1])
            self.var_roll.set(rows[2])
            self.var_course.set(rows[3])
            self.var_department.set(rows[4])
            self.var_year.set(rows[5])
            self.var_sem.set(rows[6])
            self.var_div.set(rows[7])
            self.var_gender.set(rows[8])
            self.var_date.set(rows[9])
            self.var_time.set(rows[10])
            self.var_status.set(rows[11])
        except Exception as e:
            messagebox.showerror(
                "Error", f"Error fetching data: {str(e)}", parent=self.root
            )
            self.reset_data()

    def reset_data(self):
        # Clearing entry fields
        self.var_name.set("")
        self.var_id.set("")
        self.var_roll.set("")
        self.var_course.set("")
        self.var_department.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_div.set("Select Section")
        self.var_gender.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_status.set("Select Status")

        # Deselecting all rows in Treeview widget
        selected_items = self.Attendance_report_table.selection()
        for item in selected_items:
            self.Attendance_report_table.selection_remove(item)

    def delete_data(self):
        # Confirm the action
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete all data from the Attendance.csv file?",
            parent=self.root,
        )
        if confirm:
            with open("Attendance.csv", "w", newline="") as f:
                # Clear the file content by truncating it
                f.truncate(0)

            # Clear the table view
            self.Attendance_report_table.delete(
                *self.Attendance_report_table.get_children()
            )

            messagebox.showinfo(
                "Data Deleted",
                "All data from Attendance.csv has been deleted successfully",
                parent=self.root,
            )


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
