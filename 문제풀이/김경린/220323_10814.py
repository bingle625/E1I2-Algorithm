

from collections import defaultdict
from sys import stdin

num = int(stdin.readline())

judges = defaultdict(list)
age_list = []

for i in range(num):
    age, name = stdin.readline().split()
    age = int(age)
    judges[age] .append(name)
    age_list.append(age)

for age in sorted(list(set(age_list))):
    for name in judges[age]:
        print(age,end=' ')
        print(name)


