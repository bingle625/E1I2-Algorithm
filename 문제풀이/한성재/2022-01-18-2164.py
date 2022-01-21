# 2164번 카드2

import collections


def new_deck(arr: list) -> None:

    deq = collections.deque(arr)
    while(len(deq) > 1):
        deq.popleft()
        deq.rotate(-1)

    print(deq.pop())


num = int(input())

arr = list(range(1, num+1))

new_deck(arr)
