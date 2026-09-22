# Student Management System

A simple **Student Management System** built with Python.

This project allows users to add, view, search, update, and delete student records. Student information is stored permanently in a JSON file.

## Features

* Add new student records
* View all students
* Search students by ID
* Update student information
* Delete student records
* Prevent duplicate student IDs
* Validate age
* Validate email
* Validate phone number
* Store data permanently using JSON
* Handle invalid user input
* Simple menu-driven interface

## Technologies Used

* Python 3
* JSON
* File Handling
* Dictionaries
* Functions
* Exception Handling

## Project Structure

```text
student-management-system/
│
├── student_management.py
├── students.json
├── README.md
└── requirements.txt
```

## Student Information

Each student record contains:

* Student ID
* Name
* Age
* Course
* Email
* Phone Number

Example:

```json
{
    "101": {
        "name": "Kailash",
        "age": 20,
        "course": "Computer Science",
        "email": "kailash@example.com",
        "phone": "9876543210"
    }
}
```

## Requirements

Python 3.8 or higher is recommended.

No external Python packages are required.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/student-management-system.git
```

### 2. Open the project directory

```bash
cd student-management-system
```

### 3. Run the program

```bash
python student_management.py
```

On some systems, you may need:

```bash
python3 student_management.py
```

## Menu

When the program starts, you will see:

```text
=============================================
       STUDENT MANAGEMENT SYSTEM
=============================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
=============================================
```

## How It Works

### 1. Add Student

Select:

```text
1
```

Enter the student's:

* ID
* Name
* Age
* Course
* Email
* Phone number

The record is saved automatically to `students.json`.

### 2. View Students

Select:

```text
2
```

The program displays all registered students.

### 3. Search Student

Select:

```text
3
```

Enter the student's ID.

The program displays the matching student record.

### 4. Update Student

Select:

```text
4
```

Enter the student ID.

You can modify:

* Name
* Age
* Course
* Email
* Phone

Press **Enter** without entering a value to keep the existing information.

### 5. Delete Student

Select:

```text
5
```

Enter the student ID.

The program asks for confirmation before deleting the record.

### 6. Exit

Select:

```text
6
```

The program closes safely.

## Data Storage

Student information is stored in:

```text
students.json
```

The program uses Python's built-in `json` module to read and write the records.

Because the data is stored in a file, the records remain available after closing and reopening the program.

## Example

```text
Welcome to Student Management System!

=============================================
       STUDENT MANAGEMENT SYSTEM
=============================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
=============================================

Enter your choice (1-6): 1

========== ADD STUDENT ==========
Enter student ID: 104
Enter name: Arjun
Enter age: 21
Enter course: Computer Science
Enter email: arjun@example.com
Enter phone number: 9876543213

Student added successfully!
```

## Concepts Practiced

This project is useful for learning:

* Variables
* Data types
* Dictionaries
* Functions
* Conditional statements
* Loops
* Exception handling
* File handling
* JSON
* CRUD operations
* Input validation
* Modular programming

## CRUD Operations

| Operation | Function           | Purpose                |
| --------- | ------------------ | ---------------------- |
| Create    | `add_student()`    | Add a student          |
| Read      | `view_students()`  | Display all students   |
| Read      | `search_student()` | Find a student         |
| Update    | `update_student()` | Modify student details |
| Delete    | `delete_student()` | Remove a student       |

## Future Improvements

Possible upgrades for this project:

* Add a graphical user interface using Tkinter
* Add student marks
* Calculate percentage and grade
* Search by student name
* Search by course
* Sort students by name or marks
* Export records to CSV
* Add login/authentication
* Use SQLite instead of JSON
* Create a web version using Flask
* Add a REST API
* Add a database such as MySQL

