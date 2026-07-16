import json

EMPLOYEE_FILE = "employees.json"
STUDENT_FILE = "students.json"


def load_employees():
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(employees, file)


def load_students():
    try:
        with open(STUDENT_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def insert_employee():

    employees = load_employees()

    n = int(input("Enter number of mentors: "))

    for i in range(n):

        emp_id = input("Enter Mentor ID: ")
        name = input("Enter Mentor Name: ")
        age = input("Enter Mentor Age: ")
        salary = input("Enter Mentor Salary: ")

        employees.append([
            emp_id,
            name,
            age,
            salary
        ])

    save_employees(employees)

    print("Mentor added successfully.")



def delete_employee():

    employees = load_employees()

    emp_id = input("Enter Mentor ID to delete: ")

    for emp in employees:

        if emp[0] == emp_id:

            employees.remove(emp)
            save_employees(employees)

            print("Mentor deleted successfully.")
            return

    print("Mentor not found.")



def update_employee():

    employees = load_employees()

    emp_id = input("Enter Mentor ID to update: ")

    for emp in employees:

        if emp[0] == emp_id:

            emp[1] = input("Enter New Mentor Name: ")
            emp[2] = input("Enter New Mentor Age: ")
            emp[3] = input("Enter New Mentor Salary: ")

            save_employees(employees)

            print("Mentor updated successfully.")
            return

    print("Mentor not found.")



def display_employee():

    employees = load_employees()
    students = load_students()


    if employees:

        print("\n===== MENTOR DETAILS =====")


        for emp in employees:

            print("\nMentor ID:", emp[0])
            print("Name:", emp[1])
            print("Age:", emp[2])
            print("Salary:", emp[3])


            print("Students Mentored:")

            count = 0

            for stu in students:

                if stu[4] == emp[0]:

                    print(
                        "  ",
                        stu[0],
                        "-",
                        stu[1]
                    )

                    count += 1


            if count == 0:
                print("   No students assigned")


    else:
        print("No mentors available.")



def read_employee():

    return load_employees()