import collections
from sys import stdin

k = int(stdin.readline())

queue_num = collections.deque([])

for _ in range(k):
    queue_flag = collections.deque([])

    priority = 1
    max = 0

    num = list(map(int, stdin.readline().split()))

    for i in range(num[0]):
        if i == num[1]:
            queue_flag.append(True)
        else:
            queue_flag.append(False)
    queue_num = collections.deque(list(map(int, stdin.readline().split())))

    while queue_num:
        for k in range(len(queue_num)):
            if max < queue_num[k]:
                max = queue_num[k]

        while queue_num[0] != max:
            queue_num.append(queue_num.popleft())
            queue_flag.append(queue_flag.popleft())

        if queue_flag[0] == True:
            break
        queue_num.popleft()
        queue_flag.popleft()
        priority += 1
        max = 0

    print(priority)

# 여기서 iteration 마다 queue의 순서가 바뀌어서, 해당 elem번째의 요소가 원한 데로 뽑히지 않아서 일어나는 오류
# sort함수를 사용하면 flag큐를 sortiong 할 방법이 없으므로, 내가 sort해서, flag도 같이 sort해야함.
