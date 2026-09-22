import json
import os

DATA_FILE = "students.json"


def load_students():
    """Load student records from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return data

            return {}

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read students.json. Starting with empty records.")
        return {}


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

    except OSError as error:
        print(f"Error saving student records: {error}")


def get_non_empty_input(prompt):
    """Get a non-empty string from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_valid_age():
    """Get a valid student age."""
    while True:
        try:
            age = int(input("Enter age: "))

            if 1 <= age <= 120:
                return age

            print("Age must be between 1 and 120.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_phone():
    """Get a valid phone number."""
    while True:
        phone = input("Enter phone number: ").strip()

        if phone.isdigit() and 10 <= len(phone) <= 15:
            return phone

        print("Please enter a valid phone number (10-15 digits).")


def get_valid_email():
    """Get a valid email address."""
    while True:
        email = input("Enter email: ").strip()

        if "@" in email and "." in email.split("@")[-1]:
            return email

        print("Please enter a valid email address.")


def add_student(students):
    """Add a new student."""
    print("\n========== ADD STUDENT ==========")

    student_id = get_non_empty_input("Enter student ID: ")

    if student_id in students:
        print("A student with this ID already exists.")
        return

    name = get_non_empty_input("Enter name: ")
    age = get_valid_age()
    course = get_non_empty_input("Enter course: ")
    email = get_valid_email()
    phone = get_valid_phone()

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "phone": phone
    }

    save_students(students)

    print("\nStudent added successfully!")


def view_students(students):
    """Display all student records."""
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No student records found.")
        return

    for student_id, student in students.items():
        print("-" * 40)
        print(f"Student ID : {student_id}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Course     : {student['course']}")
        print(f"Email      : {student['email']}")
        print(f"Phone      : {student['phone']}")

    print("-" * 40)
    print(f"Total students: {len(students)}")


def search_student(students):
    """Search for a student by ID."""
    print("\n========== SEARCH STUDENT ==========")

    student_id = get_non_empty_input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\nStudent Found!")
    print("-" * 40)
    print(f"Student ID : {student_id}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Course     : {student['course']}")
    print(f"Email      : {student['email']}")
    print(f"Phone      : {student['phone']}")
    print("-" * 40)


def update_student(students):
    """Update an existing student record."""
    print("\n========== UPDATE STUDENT ==========")

    student_id = get_non_empty_input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\nPress Enter to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()
    if name:
        student["name"] = name

    while True:
        age_input = input(f"Age [{student['age']}]: ").strip()

        if not age_input:
            break

        try:
            age = int(age_input)

            if 1 <= age <= 120:
                student["age"] = age
                break

            print("Age must be between 1 and 120.")

        except ValueError:
            print("Please enter a valid number.")

    course = input(f"Course [{student['course']}]: ").strip()
    if course:
        student["course"] = course

    while True:
        email = input(f"Email [{student['email']}]: ").strip()

        if not email:
            break

        if "@" in email and "." in email.split("@")[-1]:
            student["email"] = email
            break

        print("Please enter a valid email address.")

    while True:
        phone = input(f"Phone [{student['phone']}]: ").strip()

        if not phone:
            break

        if phone.isdigit() and 10 <= len(phone) <= 15:
            student["phone"] = phone
            break

        print("Please enter a valid phone number (10-15 digits).")

    save_students(students)

    print("\nStudent updated successfully!")


def delete_student(students):
    """Delete a student record."""
    print("\n========== DELETE STUDENT ==========")

    student_id = get_non_empty_input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print(f"\nStudent: {student['name']}")
    confirmation = input("Are you sure you want to delete this student? (y/n): ").strip().lower()

    if confirmation == "y":
        del students[student_id]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Delete operation cancelled.")


def display_menu():
    """Display the main menu."""
    print("\n")
    print("=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)


def main():
    """Main program."""
    students = load_students()

    print("\nWelcome to Student Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()