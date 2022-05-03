
from collections import deque
import heapq
import queue
from sys import stdin

num = int(stdin.readline())

cards = []
for i in range(num):
    card = int(stdin.readline())
    cards.append(card)

compare = 0

heapq.heapify(cards)

for i in range(num-1):

    card_1 = heapq.heappop(cards)
    card_2 = heapq.heappop(cards)
    card_sum = card_1 + card_2
    heapq.heappush(cards,card_sum)

    compare += card_sum


print(compare)