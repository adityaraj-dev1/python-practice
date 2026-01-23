students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Find Highest Marks")
    print("5. Search Student")
    print("6. Calculate Average Marks")
    print("7. Exit")

    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
        print("Student added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for i, s in enumerate(students, start=1):
                print(i, "Name:", s["name"], "| Marks:", s["marks"])

    elif choice == "3":
        name = input("Enter name to delete: ")
        found = False

        for s in students:
            if s["name"].lower() == name.lower():
                students.remove(s)
                found = True
                print("Student deleted.")
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        if len(students) == 0:
            print("No students available.")
        else:
            highest = students[0]
            for s in students:
                if s["marks"] > highest["marks"]:
                    highest = s

            print("Top Student:")
            print("Name:", highest["name"])
            print("Marks:", highest["marks"])

    elif choice == "5":
        name = input("Enter name to search: ")
        found = False

        for s in students:
            if s["name"].lower() == name.lower():
                print("Student Found:")
                print("Name:", s["name"], "| Marks:", s["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "6":
        if len(students) == 0:
            print("No students available.")
        else:
            total = 0
            for s in students:
                total += s["marks"]

            average = total / len(students)
            print("Average Marks:", average)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
