"""
Student service functions.
"""

from models.student import Student
from utils.file_handler import load_data, save_data


def add_student():
    """Add student."""

    data = load_data()

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")

    try:
        grades = list(
            map(int, input("Enter grades: ").split())
        )

    except ValueError:
        print("Invalid grades input.\n")
        return

    student = Student(student_id, name, grades)

    data.append(student.to_dict())

    save_data(data)

    print("Student added successfully!\n")


def view_students():
    """Display all students."""

    data = load_data()

    if not data:
        print("No student records found.\n")
        return

    for student in data:

        average = (
            sum(student["grades"]) /
            len(student["grades"])
        )

        print(
            f"ID: {student['student_id']} | "
            f"Name: {student['name']} | "
            f"Average: {average:.2f}"
        )

    print()


def search_student():
    """Search student by ID."""

    data = load_data()

    student_id = input("Enter Student ID: ")

    for student in data:

        if student["student_id"] == student_id:

            print("\nStudent Found:")
            print(student)
            print()
            return

    print("Student not found.\n")


def update_student():
    """Update student information."""

    data = load_data()

    student_id = input("Enter ID to update: ")

    for student in data:

        if student["student_id"] == student_id:

            new_name = input("New name: ")
            new_grades = input("New grades: ")

            if new_name:
                student["name"] = new_name

            if new_grades:

                try:
                    student["grades"] = list(
                        map(int, new_grades.split())
                    )

                except ValueError:
                    print("Invalid grades format.\n")
                    return

            save_data(data)

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    """Delete student."""

    data = load_data()

    student_id = input("Enter ID to delete: ")

    new_data = [
        student for student in data
        if student["student_id"] != student_id
    ]

    if len(new_data) == len(data):
        print("Student not found.\n")

    else:
        save_data(new_data)
        print("Student deleted successfully!\n")


def sort_students():
    """Sort students by average."""

    data = load_data()

    sorted_data = sorted(
        data,
        key=lambda student:
        sum(student["grades"]) /
        len(student["grades"]),
        reverse=True
    )

    for student in sorted_data:

        average = (
            sum(student["grades"]) /
            len(student["grades"])
        )

        print(
            f"{student['name']} "
            f"- Average: {average:.2f}"
        )

    print()