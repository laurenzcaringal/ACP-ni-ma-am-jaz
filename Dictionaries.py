import os
import json

students = {
    1: {"name": "John", "age": 19, "srCode": "24-43298"},
    2: {"name": "Jane", "age": 20, "srCode": "24-43299"},
    3: {"name": "Jack", "age": 21, "srCode": "24-43331"},
    4: {"name": "Jill", "age": 21, "srCode": "24-43332"},
    5: {"name": "Jake", "age": 21, "srCode": "24-43324"},
}

def add_student(new_id):
    name = input("Student Name: ")
    age = input("Student Age: ")
    code = input("Student Code: ")

    students[new_id] = {"name": name, "age": age, "srCode": code}
    print(f"{name} added successfully!")
    os.system("cls" if os.name == "nt" else "clear")

def show_students():
    for sid, info in students.items():
        print(f"{sid}: Name: {info['name']}, Age: {info['age']}, Code: {info['srCode']}")

def save_data():
    with open("students.txt", "w") as f:
        json.dump(students, f, indent=2)
    print("Student data saved!")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Save Data")
    print("4. Exit")

    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if choice == 1:
        add_student(len(students)+1)
    elif choice == 2:
        show_students()
    elif choice == 3:
        save_data()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
