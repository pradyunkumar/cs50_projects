import csv
import cs50
from sys import argv, exit

if len(argv) != 2:
    print("Please Enter the proper number of args")
    exit(1)
    
db = SQL("sqlite:///students.db")

