def show_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Find Highest Marks")
    print("5. Search Student")
    print("6. Calculate Average Marks")
    print("7. Exit")


def add_student(students):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']} | Marks: {student['marks']}")


def delete_student(students):
    name = input("Enter name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted.")
            return
    print("Student not found.")


def highest_marks(students):
    if not students:
        print("No students available.")
        return

    highest = max(students, key=lambda x: x["marks"])
    print("Top Student:")
    print(f"Name: {highest['name']} | Marks: {highest['marks']}")


def search_student(students):
    name = input("Enter name to search: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student Found: Name: {student['name']} | Marks: {student['marks']}")
            return
    print("Student not found.")


def find_average(students):
    if not students:
        print("No students available.")
        return

    average = sum(s["marks"] for s in students) / len(students)
    print(f"Average Marks: {average}")


def main():
    students = []

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            highest_marks(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            find_average(students)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
