import json


STUDENT_FILE = "students.json"


def load_students():

    try:

        with open(STUDENT_FILE, "r") as file:
            return json.load(file)

    except:

        return []



def save_students(students):

    with open(STUDENT_FILE, "w") as file:
        json.dump(students, file)



def insert_student():

    students = load_students()


    n = int(input("Enter number of students: "))


    for i in range(n):

        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Student Course: ")
        mentor = input("Enter Mentor ID: ")


        students.append([
            sid,
            name,
            age,
            course,
            mentor
        ])


    save_students(students)

    print("Student added successfully.")



def delete_student():

    students = load_students()


    sid = input("Enter Student ID to delete: ")


    for stu in students:

        if stu[0] == sid:

            students.remove(stu)

            save_students(students)

            print("Student deleted successfully.")
            return


    print("Student not found.")



def update_student():

    students = load_students()


    sid = input("Enter Student ID to update: ")


    for stu in students:

        if stu[0] == sid:

            stu[1] = input("Enter New Name: ")
            stu[2] = input("Enter New Age: ")
            stu[3] = input("Enter New Course: ")
            stu[4] = input("Enter New Mentor ID: ")


            save_students(students)

            print("Student updated successfully.")
            return


    print("Student not found.")



def display_student():

    students = load_students()


    if students:


        print("\n===== STUDENT DETAILS =====")

        print("ID\tName\tAge\tCourse\tMentor")


        for stu in students:

            print(
                stu[0],
                "\t",
                stu[1],
                "\t",
                stu[2],
                "\t",
                stu[3],
                "\t",
                stu[4]
            )


    else:

        print("No students available.")



def read_student():

    return load_students()