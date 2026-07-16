from employee import insert_employee, display_employee, update_employee, delete_employee


def main():

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Insert Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            insert_employee()

        elif choice == "2":
            display_employee()

        elif choice == "3":
            update_employee()

        elif choice == "4":
            delete_employee()

        elif choice == "5":
            print("Exiting Employee Management System...")
            break

        else:
            print("Invalid choice! Please enter 1 to 5.")


if __name__ == "__main__":
    main()