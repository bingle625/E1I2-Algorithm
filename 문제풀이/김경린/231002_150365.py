from collections import deque
import sys

sys.setrecursionlimit(10**8)


dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dr = ['d', 'l', 'r', 'u']

def dfs(route, x, y, r, c, k, n, m):
    if k < len(route)+abs(r-x) + abs(c-y):
        return 'impossible'
    if len(route) == k:
        if (x, y) == (r,c):
            return route
    else:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<=next_x<n and 0<=next_y<m:
                answer = dfs(route+[dr[i]], next_x, next_y, r, c, k, n, m)
                if answer != 'impossible':
                    return answer
    return 'impossible'

    

def solution(n, m, x, y, r, c, k):
    
    if k < abs(r-x) + abs(c-y) or ((k - (abs(r-x) + abs(c-y))) % 2 == 1):
        return 'impossible'

    x -= 1
    y -= 1
    r -= 1
    c -= 1
    
    answer = dfs([], x, y, r, c, k, n, m)


    return ''.join(answer) if answer != 'impossible' else answer

