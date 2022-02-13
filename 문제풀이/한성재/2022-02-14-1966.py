import collections
from sys import stdin

k = int(stdin.readline())

queue_num = collections.deque([])
queue_flag = collections.deque([])

for _ in range(k):
    num = list(map(int, stdin.readline().split()))

    for i in range(num[0]):
        if i == num[1]:
            queue_flag.appendleft(True)
        else:
            queue_flag.appendleft(False)
    queue_num = collections.deque(list(map(int, stdin.readline().split())))

    if queue_num[-1]

print(num)
print(queue_flag)
