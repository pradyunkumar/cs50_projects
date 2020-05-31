from sys import argv, exit
import cs50

if len(argv) != 2:
    print("Please print correct number of args")
    exit(1)
    
house = argv[1]
db = cs50.SQL("sqlite:///students.db")
students = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last ASC, first ASC", house)

for student in students:
    print("{0} {1}, born {2}".format(student["first"], student["last"], student["birth"]))