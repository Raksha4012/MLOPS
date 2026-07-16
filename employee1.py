# employee.py

employee_data = []

def add_employees():
    n = int(input("Enter number of employees: "))

    for i in range(n):
        print(f"\nEmployee {i+1}")
        name = input("Enter Name: ")
        dept = input("Enter Department (CSE/ECE/EEE): ").upper()
        expense = float(input("Enter Expense/Salary: "))

        employee_data.append({
            "name": name,
            "dept": dept,
            "expense": expense
        })

    return employee_data