from random import choice

employees = []

match choice:

    case 1:
        employee = {"id": int(input("Enter Employee ID: ")), "name": input("Enter Employee Name: "),
                    "department": input("Enter Employee Department: "), "salary": int(input("Enter Employee Salary: "))}

        employees.append(employee)
        print("Employee added successfully.")

    case 2:
        if len(employees) == 0:
            print("No employees found.")
        else:
            print("\nEmployee List")
            for employee in employees:
                print("Employee ID:", employee["id"])
                print("Employee Name:", employee["name"])
                print("Employee Department:", employee["department"])
                print("Employee Salary:", employee["salary"])
                print("---------------------------")