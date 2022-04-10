#10816 숫자 카드 2

import collections
from sys import stdin, stdout

number = int(input())

cards = list(map(int,stdin.readline().rstrip().split()))

cards = collections.Counter(cards)

number2 = int(input())

target = list(map(int,stdin.readline().rstrip().split()))
result = []
cardsList = list(cards.keys())

for item in target:
    if item not in cards:
        result.append(0)
    else:
        result.append(cards[item])
                
for targetItem in result:
    print(targetItem,end=" ")