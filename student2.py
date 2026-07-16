# student.py

student_data = []


def get_student_data():

    n = int(input("Enter number of students: "))

    for i in range(n):

        print("\nStudent", i+1)

        name = input("Enter student name: ")
        department = input("Enter department (CSE/ECE/EEE): ").upper()
        fee = float(input("Enter course fee: "))

        student_data.append({
            "name": name,
            "department": department,
            "fee": fee
        })

    return student_data