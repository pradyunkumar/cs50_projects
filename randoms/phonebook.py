from sys import exit

# dictionary
people = {
    "EMMA": "382432984",
    "RODRIGO": "291409221",
    "BRIAN": "287393021",
    "DAVID": "281348031"
}

if "EMMA" in people:
    print(f"Found {people['EMMA']}")    #single quotes are needed as "" also used
    exit(0)
print("Not found")
exit(1)