import csv
import student


def csv_convert():

    students = student.read_student()

    if not students:
        print("No student data found.")
        return

    print("\n===== STUDENT INFORMATION =====")
    print("ID\tName\tAge\tCourse")
    print("-" * 40)

    for stu in students:
        print(f"{stu[0]}\t{stu[1]}\t{stu[2]}\t{stu[3]}")

    with open("student.csv", "w", newline="") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Student ID",
            "Student Name",
            "Student Age",
            "Student Course"
        ])

        for stu in students:
            writer.writerow(stu)

    print("\nStudent data successfully exported.")


if __name__ == "__main__":
    csv_convert()