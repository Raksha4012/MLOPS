import json

FILE_NAME = "employees.json"


def load_employees():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file)


def insert_employee():
    employees = load_employees()

    n = int(input("Enter the number of employees: "))

    for i in range(n):
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        age = input("Enter Employee Age: ")
        salary = input("Enter Employee Salary: ")

        employees.append([eid, name, age, salary])

    save_employees(employees)

    print("Employees added successfully.")


def delete_employee():
    employees = load_employees()

    eid = input("Enter Employee ID to delete: ")

    for employee in employees:
        if employee[0] == eid:
            employees.remove(employee)
            save_employees(employees)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")


def update_employee():
    employees = load_employees()

    eid = input("Enter Employee ID to update: ")

    for employee in employees:
        if employee[0] == eid:
            employee[1] = input("Enter New Employee Name: ")
            employee[2] = input("Enter New Employee Age: ")
            employee[3] = input("Enter New Employee Salary: ")

            save_employees(employees)

            print("Employee updated successfully.")
            return

    print("Employee not found.")


def display_employee():
    employees = load_employees()

    if employees:
        print("\n===== EMPLOYEE RECORDS =====")
        print("ID\tName\tAge\tSalary")

        for employee in employees:
            print(f"{employee[0]}\t{employee[1]}\t{employee[2]}\t{employee[3]}")
    else:
        print("No employees available.")


def read_employee():
    return load_employees()