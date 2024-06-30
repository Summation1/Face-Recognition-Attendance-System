# Face-Recognition-Attendance-System

Steps to run the code 

1st:-   create a folder named face recognition system and put all the files there.
2nd :- create an empty folder named data in the face recognition system folder,it will store all the upload images of student.
3rd:- make sure to install all the pythons libraries that I have imported in the files.Otherwise it will give you error
4th :- create databases
   .You need to create 2 databases 1 for login page and 2nd one for students details 

  . create a schema first named face_recogniser
  . then add 2 table 
  . 1st is register for login page  just run this code
  
   USE face_recogniser;

CREATE TABLE register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    security_question VARCHAR(100) NOT NULL,
    security_answer VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);


. 2nd is for student details named  student just run below code to create the table 

   USE Face_Recogniser;


   CREATE TABLE IF NOT EXISTS student (
    course VARCHAR(50),
    department VARCHAR(50),
    year INT,
    semester INT,
    student_id VARCHAR(20),
    student_name VARCHAR(100),
    division VARCHAR(10),
    roll_number VARCHAR(20),
    gender VARCHAR(10),
    dob DATE,
    email VARCHAR(100),
    phone VARCHAR(15),
    address TEXT,
    teacher VARCHAR(100),
    radio_value INT,
    PRIMARY KEY (student_id)
);

. Now you need to integrate it with python file in the login.py file and student.py file 
  
   import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivanshu@123",
    database="face_recogniser"
)

# Use 'conn' to create cursor and execute queries

. This code is already exist in file you just need to change the details according to your database like user or password 












   
