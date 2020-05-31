
from cs50 import get_int

# for i in range(4):
#     print("?", end = "")    #changes the end
# print("?" * 4)  #pythonic way
# print()
# # for i in range(3):
# #     print("#")
# print("#\n" * 3, end="")
# print()

# for i in range(3):
#     for j in range(3):
#         print("#", end = "")
#     print()

while True:
    i = get_int("Height: ")
    if i in range(1, 9):
        break

for a in range(1, i + 1):
    for x in range(i - a):
        print(" ", end = "")
    for y in range(a):
        print("#", end = "")
    print()