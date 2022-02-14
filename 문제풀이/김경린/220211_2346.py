from collections import deque


class Node:
    def __init__(self, index, num):
        self.index = index
        self.num = num


def bubble_pop(ballons):
    end = 0

    ballon_num = ballons[0].num
    ballons.popleft()
    print('1 ', end='')
    if ballon_num > 0:
        ballon_num -= 1
    else:
        ballon_num = (ballon_num + len(ballons)) % len(ballons)

    while ballons:
        for i in range(ballon_num):
            tmp = ballons.popleft()
            ballons.append(tmp)
        tmp = ballons.popleft()
        print(tmp.index, end=' ')
        if not ballons:
            break
        ballon_num = tmp.num
        if ballon_num < 0:
            ballon_num = (ballon_num + len(ballons)) % len(ballons)
        else:
            ballon_num -= 1


num = int(input())
ballons_nums = list(map(int, input().split()))
ballons = deque()
for i in range(num):
    ballons.append(Node(i+1, ballons_nums[i]))

bubble_pop(ballons)
