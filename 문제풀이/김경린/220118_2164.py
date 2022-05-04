from collections import deque


def last_card(cards: deque):
    while len(cards) > 1:
        cards.popleft()
        top = cards.popleft()
        cards.append(top)
    return cards.pop()


num = int(input())
cards = deque(range(1, num+1))

print(last_card(cards))
