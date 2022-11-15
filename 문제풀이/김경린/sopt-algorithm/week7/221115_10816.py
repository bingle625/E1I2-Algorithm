from collections import defaultdict
from sys import stdin

cardNum = int(stdin.readline())
cards = list(map(int, stdin.readline().split(' ')))

targetNum = int(stdin.readline())
targetCards = list(map(int, stdin.readline().split(' ')))

cardInfo = defaultdict(int)
for i in cards:
    cardInfo[i] += 1

for target in targetCards:
    print(cardInfo[target], end=' ')

# cards.sort()


# for target in targetCards:
#     left = 0
#     right = cardNum - 1
#     flag = 0
#     while left<=right:
#         idx = (left + right)//2
#         if cards[idx] == target:
#             print(cards[left:right+1].count(target), end = ' ')
#             flag = 1
#             break
#         if cards[idx] < target:
#             left = idx + 1
#         if cards[idx] > target:
#             right = idx - 1
#     if flag == 0:
#         print(0, end=' ')

