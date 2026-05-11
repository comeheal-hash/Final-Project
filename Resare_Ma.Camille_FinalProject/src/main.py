"""
Main application file.
"""

from services.student_service import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    sort_students
)


def login():
    """Simple login system."""

    USERNAME = "admin"
    PASSWORD = "1234"

    print("===== LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin successful!\n")
        return True

    print("\nInvalid username or password.\n")
    return False


def menu():
    """Display menu."""

    while True:

        print("===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            sort_students()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


def main():
    """Main function."""

    if login():
        menu()


if __name__ == "__main__":
    main()