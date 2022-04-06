#2920

from sys import stdin

str = stdin.readline().rstrip()

if str == "1 2 3 4 5 6 7 8":
    print("ascending")
elif str == "8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")