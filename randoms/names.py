from sys import exit

names = ["EMMA", "RODRIGO", "BRIAN", "DAVID"]

if "EMMA" in names:
    print("found")
    exit(0)
print("Not found")
exit(1)