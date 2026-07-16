# student.py

student_data = []

def add_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nStudent {i+1}")
        name = input("Enter Name: ")
        dept = input("Enter Department (CSE/ECE/EEE): ").upper()
        fee = float(input("Enter Fee: "))

        student_data.append({
            "name": name,
            "dept": dept,
            "fee": fee
        })

    return student_data