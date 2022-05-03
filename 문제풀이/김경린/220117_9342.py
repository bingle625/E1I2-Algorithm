import re


def match_pattern(strs):
    p = re.compile('[A-F]?A+F+C+[A-F]?$')
    if p.match(strs):
        return "Infected!"
    else:
        return "Good"


case = int(input())
for i in range(case):
    strs = input()
    print(match_pattern(strs))
