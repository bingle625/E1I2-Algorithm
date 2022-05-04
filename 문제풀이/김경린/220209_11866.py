from audioop import reverse
from collections import deque


def josephus(k: int, group: deque):
    removed = []
    while group:
        for i in range(k-1):
            src = group.popleft()
            group.append(src)
        removed.append(group.popleft())
    return removed


n, k = map(int, input().split())
group = deque([i for i in range(1, n+1)])
removed = josephus(k, group)

print('<', end='')
for i in range(len(removed)-1):
    print(removed[i], end=', ')
print(removed[len(removed)-1], end='')
print('>')
