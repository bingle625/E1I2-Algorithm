
# 0:[1] 1 + 1
# 1:[0, 2] 2 + 1
# 2:[1, 3] 2 + 1 + 1
# 3:[2, 4]
# 4:[3]


from collections import defaultdict
from sys import stdin


n = int(stdin.readline())
friends = [[] for _ in range(n)]
graph = defaultdict(list)
for i in range(n):
    friends[i] = list(stdin.readline().rstrip())
    for j in range(n):
        if friends[i][j] == 'Y':
            graph[i].append(j)

for i in range(n):
    for j in graph[i]:
        for k in graph[j]:
            if friends[i][k] == 'N' and i != k:
                friends[i][k] = 'Y'

max_cnt = 0
for i in range(n):
    max_cnt = max(max_cnt, friends[i].count('Y'))

# print(friends)
print(max_cnt)