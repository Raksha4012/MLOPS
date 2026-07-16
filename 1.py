#from script3 import insert_employee, delete_employee, update_employee, display_employee
import employee
employee.employees

def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Display")
        print("5. Exit")

        c = int(input("Enter the action you want to perform: "))

        match c:
            case 1:
                employee.insert_employee()

            case 2:
                employee.delete_employee()

            case 3:
                employee.update_employee()

            case 4:
                employee.display_employee()

            case 5:
                print("Exiting...")
                break

            case _:
                print("Invalid choice.")

main()