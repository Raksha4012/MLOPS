import employee
from os import write
data= employee.read()
print(data)

read - r
write() - w
read and write() - r+
append - a
file("File_name",mode)
file.close()
with open("File_name","r") as db:
    print(db.read())
    db.close()
