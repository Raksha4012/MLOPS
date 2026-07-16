from student import insert_student, display_student, update_student, delete_student


def main():

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Insert Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            insert_student()

        elif choice == "2":
            display_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting Student Management System...")
            break

        else:
            print("Invalid choice! Please enter 1 to 5.")


if __name__ == "__main__":
    main()