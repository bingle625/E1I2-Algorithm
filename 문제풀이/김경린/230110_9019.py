from collections import deque
from sys import stdin

def D(n, command):
    n *= 2
    if n>9999:
        n %= 10000
    return n, command+'D'

def S(n, command):
    if n == 0:
        n = 9999
        return n, command+'S'
    return n-1, command+'S'

def L(n, command):
    n = str(n)
    n = '0'*(4-len(n)) + n
    return int(n[1:]+n[0]), command+'L'

def R(n, command):
    n = str(n)
    n = '0'*(4-len(n)) + n
    return int(n[-1]+n[:-1]), command+'R'

def_list = [D, S, L, R]

def bfs(num,target):
    visited = [ 0 for _ in range(10000)]
    num_deque = deque()
    num_deque.append((num, ''))
    visited[num] = 1
    while len(num_deque):
        n, command = num_deque.popleft()
        if n == target:
            return command
        for func in def_list:
            new_n, new_command = func(n, command)
            if visited[new_n] == 0:
                visited[new_n] = 1
                num_deque.append((new_n, new_command))

case = int(stdin.readline())
for i in range(case):
    num, target = map(int, stdin.readline().rstrip().split())
    print(bfs(num, target))

