# employee.py

employee_data = []


def get_employee_data():

    n = int(input("Enter number of employees: "))

    for i in range(n):

        print("\nEmployee", i+1)

        name = input("Enter employee name: ")
        department = input("Enter department (CSE/ECE/EEE): ").upper()
        salary = float(input("Enter salary: "))
        capacity = int(input("Enter mentor capacity: "))

        employee_data.append({
            "name": name,
            "department": department,
            "salary": salary,
            "capacity": capacity
        })

    return employee_data