# Face Recognition Attendance System

## Overview

The Face Recognition Attendance System is a project designed to automate the attendance marking process using facial recognition technology. It allows users to register, log in securely, and manage student attendance records efficiently.

## Features

### 1. Registration and Login
- **Registration:** Users can register by providing basic details such as name, contact number, email, and security information (security question and answer). This information is stored securely in the `register` table in the database.
  
- **Login:** Registered users can log in using their email and password. The system verifies the credentials against the `register` table in the database.

### 2. Student Management
- **Add Students:** Authorized users (e.g., teachers, administrators) can add students to the system. Each student is associated with details like course, department, year, semester, student ID, name, gender, date of birth, contact information, and more. This information is stored in the `student` table in the database.
  
- **View and Update Students:** Users can view and update student details as necessary, such as editing contact information or assigning a new teacher.

### 3. Face Recognition for Attendance
- **Automatic Attendance Marking:** The core feature of the system is the ability to mark attendance using face recognition. Here's how it works:
  
  - **Enrollment:** During student enrollment, the system captures multiple images of the student's face, which are stored in the `data` folder.
  
  - **Recognition:** When marking attendance, the system captures the current image of the student and compares it with the stored images using OpenCV and face recognition algorithms. If a match is found, attendance is marked for that student.
  
  - **Logging Attendance:** Successful attendance records are logged in the database with details such as date, time, student ID, and course information.

### 4. Forgot Password and Security Features
- **Forgot Password:** Users can reset their password using a security question and answer combination stored during registration.
  
- **Security Measures:** The system ensures data security by storing passwords securely hashed and uses security questions to verify user identity.

## Integration and Technologies Used

### 1. Technologies
- **Python:** Used for backend logic, face recognition using OpenCV, and GUI using tkinter.
  
- **MySQL:** Database management system for storing user and student information securely.

### 2. Integration with Python Files
- **Database Connection:** Python files (`login.py`, `student.py`) are integrated with MySQL database for storing and retrieving user and student data.

## Future Enhancements
- **Enhanced UI:** Improve the user interface for better usability.
  
- **Attendance Reports:** Generate detailed reports for attendance statistics.
  
- **Real-time Updates:** Implement real-time attendance updates for better monitoring.

## Usage
To use the Face Recognition Attendance System:
- Ensure all dependencies are installed (`opencv-python`, `Pillow`, `mysql-connector-python`).
- Set up MySQL database with required tables (`register`, `student`).
- Run the main Python file (`main.py`) to start the application.

## Conclusion
The Face Recognition Attendance System simplifies attendance management through automated face recognition technology, enhancing efficiency and accuracy in educational and organizational settings.

Feel free to explore and customize this system further based on your specific needs and requirements.
