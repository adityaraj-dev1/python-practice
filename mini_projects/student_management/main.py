students = []

def show_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Find Highest Marks")
    print("5. Search Student")
    print("6. Calculate Average Marks")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
        print("Student added successfully.")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for i, student in enumerate(students, start=1):
                print(i, "Name:", student["name"], "| Marks:", student["marks"])

    elif choice == "3":
        name = input("Enter name to delete: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                found = True
                print("Student deleted.")
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No students available.")
        else:
            highest = students[0]
            for student in students:
                if student["marks"] > highest["marks"]:
                    highest = student

            print("Top Student:")
            print("Name:", highest["name"])
            print("Marks:", highest["marks"])

    elif choice == "5":
        name = input("Enter name to search: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print("Student Found:")
                print("Name:", student["name"], "| Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "6":
        if not students:
            print("No students available.")
        else:
            total = 0
            for student in students:
                total += student["marks"]

            average = total / len(students)
            print("Average Marks:", average)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
