# main.py

import matplotlib.pyplot as plt
from student1 import add_students
from employee1   import add_employees

students = add_students()
employees = add_employees()

departments = ["CSE", "ECE", "EEE"]

fee_total = {
    "CSE": 0,
    "ECE": 0,
    "EEE": 0
}

expense_total = {
    "CSE": 0,
    "ECE": 0,
    "EEE": 0
}

# Calculate total fees
for s in students:
    if s["dept"] in fee_total:
        fee_total[s["dept"]] += s["fee"]

# Calculate total expenses
for e in employees:
    if e["dept"] in expense_total:
        expense_total[e["dept"]] += e["expense"]

print("\nDepartment-wise Fee Collection")
for d in departments:
    print(d, ":", fee_total[d])

print("\nDepartment-wise Employee Expense")
for d in departments:
    print(d, ":", expense_total[d])

# Net amount (Fee - Expense)
net = []
for d in departments:
    net.append(fee_total[d] - expense_total[d])

colors = ["red", "blue", "yellow"]

plt.figure(figsize=(7,5))
plt.bar(departments, net, color=colors)

plt.title("Department-wise Net Amount")
plt.xlabel("Department")
plt.ylabel("Fee - Employee Expense")

plt.show()