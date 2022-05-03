# 나이순 정렬

import collections
from sys import stdin



number = int(input())
dic = collections.defaultdict(list)

for _ in range(number):
    age,Name = stdin.readline().rstrip().split()
    age = int(age)
    dic[age].append(Name)

ages = list(dic.keys())
ages.sort()

for age in ages:
    for name in dic[age]:
        print(age,name)