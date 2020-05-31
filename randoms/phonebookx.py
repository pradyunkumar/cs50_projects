import csv
from cs50 import get_string

# file = open("phonebook.csv", "a")

name = get_string("Name: ")
number = get_string("Number: ")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)   #pass open file to library to make reading easier
    writer.writerow((name, number))
# no need to close with with