from student import (
    insert_student,
    display_student,
    update_student,
    delete_student
)

from employee import (
    insert_employee,
    display_employee,
    update_employee,
    delete_employee
)



def main():


    while True:


        print("\n===== MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Mentor Management")
        print("3. Exit")


        choice = input("Enter choice: ")



        if choice == "1":

            while True:

                print("\n--- STUDENT MENU ---")
                print("1. Add Student")
                print("2. Display Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Back")


                ch = input("Enter choice: ")


                if ch == "1":
                    insert_student()

                elif ch == "2":
                    display_student()

                elif ch == "3":
                    update_student()

                elif ch == "4":
                    delete_student()

                elif ch == "5":
                    break



        elif choice == "2":


            while True:

                print("\n--- MENTOR MENU ---")
                print("1. Add Mentor")
                print("2. Display Mentor With Students")
                print("3. Update Mentor")
                print("4. Delete Mentor")
                print("5. Back")


                ch = input("Enter choice: ")


                if ch == "1":
                    insert_employee()

                elif ch == "2":
                    display_employee()

                elif ch == "3":
                    update_employee()

                elif ch == "4":
                    delete_employee()

                elif ch == "5":
                    break



        elif choice == "3":

            print("Thank you")
            break


        else:

            print("Invalid choice")



if __name__ == "__main__":
    main()