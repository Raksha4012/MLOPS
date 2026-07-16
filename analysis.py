# analysis.py

import matplotlib.pyplot as plt
from employee2 import get_employee_data
from student2 import get_student_data


# Get input from employee and student modules

employees = get_employee_data()
students = get_student_data()


departments = ["CSE", "ECE", "EEE"]


# -----------------------------
# Initialize department storage
# -----------------------------

report = {}

for dept in departments:

    report[dept] = {

        "salary":0,
        "fee":0,
        "students":0,
        "mentor_capacity":0,
        "mentors":0
    }



# -----------------------------
# Calculate Employee Details
# -----------------------------

for emp in employees:

    dept = emp["department"]

    if dept in report:

        report[dept]["salary"] += emp["salary"]

        report[dept]["mentor_capacity"] += emp["capacity"]

        report[dept]["mentors"] += 1



# -----------------------------
# Calculate Student Details
# -----------------------------

for stu in students:

    dept = stu["department"]

    if dept in report:

        report[dept]["fee"] += stu["fee"]

        report[dept]["students"] += 1



# -----------------------------
# Merge and Analysis
# -----------------------------

print("\n========== Department Analysis ==========")


profit = []
students_count = []
capacity = []
utilization = []
student_ratio = []


for dept in departments:


    salary = report[dept]["salary"]

    fee = report[dept]["fee"]

    total_students = report[dept]["students"]

    mentor_capacity = report[dept]["mentor_capacity"]

    mentors = report[dept]["mentors"]



    # Profit / Loss

    result = fee - salary



    # Capacity utilization

    if mentor_capacity > 0:

        util = (total_students / mentor_capacity) * 100

    else:

        util = 0



    # Student per mentor

    if mentors > 0:

        ratio = total_students / mentors

    else:

        ratio = 0



    print("\nDepartment:", dept)

    print("-------------------------")

    print("Total Salary :", salary)

    print("Total Fee :", fee)

    print("Profit/Loss :", result)

    print("Total Students :", total_students)

    print("Total Mentors :", mentors)

    print("Total Mentor Capacity :", mentor_capacity)

    print("Capacity Utilization :", round(util,2),"%")

    print("Student per Mentor :", round(ratio,2))



    # Mentor suggestion

    if total_students > mentor_capacity:


        shortage = total_students - mentor_capacity

        avg_capacity = 30

        required = (shortage + avg_capacity - 1)//avg_capacity


        print("Suggestion : Add",required,"more mentor(s)")


    else:

        print("Suggestion : Current mentors are sufficient")



    profit.append(result)

    students_count.append(total_students)

    capacity.append(mentor_capacity)

    utilization.append(util)

    student_ratio.append(ratio)



# -----------------------------
# Plot 1 Profit/Loss
# -----------------------------


plt.figure(figsize=(7,5))

plt.bar(
    departments,
    profit,
    color=["red","blue","yellow"]
)

plt.title("Department Profit/Loss")

plt.xlabel("Department")

plt.ylabel("Amount")

plt.axhline(0,color="black")

plt.show()



# -----------------------------
# Plot 2 Student vs Capacity
# -----------------------------


x = range(len(departments))


plt.figure(figsize=(7,5))


plt.bar(
    x,
    students_count,
    width=0.4,
    label="Students",
    color="green"
)


plt.bar(
    [i+0.4 for i in x],
    capacity,
    width=0.4,
    label="Mentor Capacity",
    color="orange"
)


plt.xticks(
    [i+0.2 for i in x],
    departments
)


plt.title("Student Count vs Mentor Capacity")

plt.ylabel("Count")

plt.legend()

plt.show()



# -----------------------------
# Plot 3 Capacity Utilization
# -----------------------------


plt.figure(figsize=(7,5))


plt.bar(
    departments,
    utilization,
    color=["red","blue","yellow"]
)


plt.axhline(
    100,
    color="black",
    linestyle="--"
)


plt.title("Capacity Utilization")

plt.ylabel("Percentage")


plt.show()



# -----------------------------
# Plot 4 Student Mentor Ratio
# -----------------------------


plt.figure(figsize=(7,5))


plt.bar(
    departments,
    student_ratio,
    color=["red","blue","yellow"]
)


plt.title("Student Per Mentor")

plt.ylabel("Students")


plt.show()