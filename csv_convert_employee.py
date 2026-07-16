import csv
import employee


def csv_convert():

    employees = employee.read_employee()

    if employees is None or len(employees) == 0:
        print("No employee data found.")
        return

    print("\n===== EMPLOYEE INFORMATION =====")
    print("ID\tName\tAge\tSalary")
    print("-" * 40)

    for emp in employees:
        print(f"{emp[0]}\t{emp[1]}\t{emp[2]}\t{emp[3]}")

    with open("employee.csv", "w", newline="") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Employee ID",
            "Employee Name",
            "Employee Age",
            "Employee Salary"
        ])

        for emp in employees:
            writer.writerow([
                emp[0],
                emp[1],
                emp[2],
                emp[3]
            ])

    print("\nEmployee data successfully exported.")


if __name__ == "__main__":
    csv_convert()