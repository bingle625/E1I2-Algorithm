# N: 단어의 개수, K: 가르칠 글자

import collections

N, M = map(int, input().split())
words = list(input() for _ in range(N))

if M < 5:
    print(0)
    exit()
elif M == 26:
    print(N)
    exit()

result = 0
basic = 'antic'
learn = []

for i, word in enumerate(words):
    word = word[4:-4]
    learn.append([])

    for char in word:
        if char not in basic:
            learn[i].expand(char)

print(result)