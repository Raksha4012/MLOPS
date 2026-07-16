import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)


def insert_student():
    students = load_students()

    n = int(input("Enter the number of students: "))

    for i in range(n):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Student Course: ")

        students.append([sid, name, age, course])

    save_students(students)

    print("Students added successfully.")


def delete_student():
    students = load_students()

    sid = input("Enter Student ID to delete: ")

    for student in students:
        if student[0] == sid:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def update_student():
    students = load_students()

    sid = input("Enter Student ID to update: ")

    for student in students:
        if student[0] == sid:
            student[1] = input("Enter New Student Name: ")
            student[2] = input("Enter New Student Age: ")
            student[3] = input("Enter New Student Course: ")

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student not found.")


def display_student():
    students = load_students()

    if students:
        print("\n===== STUDENT RECORDS =====")
        print("ID\tName\tAge\tCourse")

        for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}")
    else:
        print("No students available.")


def read_student():
    return load_students()