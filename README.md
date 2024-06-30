                                       
# Face Recognition Attendance System

## Overview:
- This project implements a face recognition system for managing attendance using Python with tkinter for GUI and MySQL for database management.

## Steps to run the code
### 1. Setting Up the Project
- Clone the Repository:
 Clone the repository to your local machine:

            git clone <repository_url>

- Organize Files:
Create a folder named face_recognition_system and place all project files there.

- Create Data Folder:
Inside face_recognition_system, create an empty folder named data. This folder will store uploaded student images.

### 2. Install Required Libraries
- Ensure all Python libraries used in the project are installed:

        pip install mysql-connector-python pillow opencv-python numpy

### 3. Setting Up Databases
  
### 4. Creating MySQL Databases and Tables

## Login Page Database (face_recogniser)

- Connect to MySQL and create the face_recogniser schema:

### Code 

    CREATE DATABASE IF NOT EXISTS face_recogniser

- `Login register` Database
-  Connect to MySQL and create the Face_Recogniser schema:

  ### code


     USE face_recogniser;

     CREATE TABLE register
    (
       id INT AUTO_INCREMENT PRIMARY KEY,
    
       first_name VARCHAR(50) NOT NULL,
    
       last_name VARCHAR(50) NOT NULL,
    
       contact_no VARCHAR(15) NOT NULL,
    
       email VARCHAR(100) UNIQUE NOT NULL,
       
       security_question VARCHAR(100) NOT NULL,
    
       security_answer VARCHAR(100) NOT NULL,
    
       password VARCHAR(100) NOT NULL
    
    );


- `Student Details` Database (Face_Recogniser)


- Connect to MySQL and create the Face_Recogniser schema:

### Code 


    USE Face_Recogniser;



    CREATE TABLE IF NOT EXISTS student
    (

       course VARCHAR(50),
    
       department VARCHAR(50),
    
       year INT,
    
       semester INT,
    
       student_id VARCHAR(20) PRIMARY KEY,
    
       student_name VARCHAR(100),
    
       division VARCHAR(10),
    
       roll_number VARCHAR(20),
    
       gender VARCHAR(10),
    
       dob DATE,

       email VARCHAR(100),
    
       phone VARCHAR(15),
    
       address TEXT,
    
       teacher VARCHAR(100),
    
       radio_value INT
    
    );

## Integrating with Python Files

- Ensure the login.py and student.py files are correctly configured to connect to your MySQL database:


- import mysql.connector

## Connect to MySQL


    conn = mysql.connector.connect
    (

      host="localhost",
    
      user="root",
    
      password="YourMySQLPassword",
    
      database="face_recogniser"
    
    )

## Use 'conn' to create cursor and execute queries
### 5. Running the Application:
- Execute the main application file (main.py or login.py) to start the Face Recognition Attendance System:

