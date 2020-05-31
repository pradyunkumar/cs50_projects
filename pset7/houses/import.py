import csv
import cs50
from sys import argv, exit

if len(argv) != 2:
    print("Please Enter the proper number of args")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

with open(argv[1], "r") as students:
    reader = csv.DictReader(students)

    for row in reader:
        names = row["name"].split(" ")

        firstname = names[0]
        if len(names) == 2:
            middlename = None
            lastname = names[1]
        else:
            middlename = names[1]
            lastname = names[2]

        house = row["house"]
        birth = int(row["birth"])

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(%s, %s, %s, %s, %s)",
            (firstname, middlename, lastname, house, birth))


exit(0)


