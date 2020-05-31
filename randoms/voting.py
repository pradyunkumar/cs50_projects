import csv

# counts = dict()
ttwinners = {}

with open("Voting.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        winner = row["TT"].lower()
        
        if winner in ttwinners:
            ttwinners[winner] += 1
        else:
            ttwinners[winner] = 1
            
def f(item):
    return item[1]  # the [0] returns key and [1] returns value
    
for winner, count in sorted(ttwinners.items(), key=lambda item: item[1], reverse=True): #key=f#, reverse=True):
    print(winner, count, sep = " | ")