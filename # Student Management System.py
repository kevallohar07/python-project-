# Student Management System

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Branch": branch,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for s in students:
            print(s)


def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["Roll"] == roll:
            print("Student Found:", s)
            return
    print("Student not found.\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")