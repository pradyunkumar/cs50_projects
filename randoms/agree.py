from cs50 import get_string
import re

s = get_string("Do you agree?\n")

# if s == "Y" or s == "y":
#     print("Agreed.")
# elif s == "N" or s == "n":
#     print("Not Agreed.")

# if s.lower() in ["y", "yes"]:
#     print("Agreed.")
# elif s.lower() in ["n", "no", "nope"]:
#     print("Disagreed.")

if re.search("^y(es)?$", s.lower()): # ^ means it must start with y and $ means it must end
    print("agreed")
if re.search("n(o)?", s, re.IGNORECASE):
    print("not agreed")