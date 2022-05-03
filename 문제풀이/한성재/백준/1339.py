import collections
from sys import stdin


num = int(input())

dic = collections.defaultdict(list)
res = dict()

for _ in range(num):
    str = list(stdin.readline().rstrip())
    str.reverse()
    for i in range(len(str)):
        dic[str[i]].append(i)

for char in dic.keys():
    sum = 0 
    for number in dic[char]:
        sum += 10 ** number
    res[char] =sum

 
resultArr = sorted(list(res.values()))

result = 0

digit = 9
while resultArr:
    result += resultArr.pop() * digit
    digit -= 1

print(result)