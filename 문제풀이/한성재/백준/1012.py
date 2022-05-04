# 1012번 유기농 배추

from collections import deque
from sys import stdin


# # 내 풀이
# testCase = int(input())

# for _ in range(testCase):
#     M, N, K = map(int, stdin.readline().rstrip().split())
#     wormPlace = dict([])
#     island = 0
#     for i in range(K):
#         x, y = map(int, stdin.readline().rstrip().split())
#         wormPlace[(x,y)] = True
    
#     for i in range(M):
#         for j in range(N):
#             if (i,j) in wormPlace:
#                 island += 1
#                 stack = deque([(i,j)])
#                 while stack:

#                     if stack[0] in wormPlace:
#                         a, b = stack[0][0], stack[0][1]
#                         wormPlace.pop(stack.popleft())
#                         stack.append((a+1,b))
#                         stack.append((a-1,b))
#                         stack.append((a,b+1))
#                         stack.append((a,b-1))
#                     else:
#                         stack.popleft()
#     print(island)

# 이 문제 2등의 풀이

# tc = int(input())

# def dfs(arr,x,y,xLimit,yLimit):
#     arr[y][x] = 0
    
#     if x+1 < xLimit and arr[y][x+1] == 1:
#         dfs(arr,x+1,y,xLimit,yLimit)
#     if x-1 >= 0  and arr[y][x-1] == 1:
#         dfs(arr,x+1,y,xLimit,yLimit)
#     if y+1 < yLimit and arr[y+1][x] == 1:
#         dfs(arr,x,y+1,xLimit,yLimit)
#     if y-1 >= 0 and arr[y-1][x] == 1:
#         dfs(arr,x,y-1,xLimit,yLimit)
        
# for _ in range(tc):
#     M, N, K = map(int, stdin.readline().rstrip().split())
#     island = 0
#     arr1 = [[0] * M for _ in range(N)]
    
#     for _ in range(K):
#         x,y = map(int, stdin.readline().rstrip().split())
#         arr1[y][x] = 1
#     for i in range(M):
#         for j in range(N):
#             if arr1[j][i] == 1:
#                 island += 1
#                 dfs(arr1,i,j,M,N)
    
#     print(island)
p=stdin.readline;
q=int(p())
def T(t, o, s):
    t[s][o]=0
    if o+1 < x and t[s][o+1]==1:
        T(t,o+1,s)
    if o-1>= 0 and t[s][o-1]==1:
        T(t, o-1,s)
    if s -1 >= 0 and t[s-1][o]==1:
        T(t, o,s-1)
    if s +1 < y and t[s+1][o]==1:
        T(t,o,s+1)

for _ in range(q):
    x, y, c = map(int, p().split())
    t = [[0] * x for _ in range(y)]
    for i in range(0,c):
        m,n=map(int,p().split());t[n][m] = 1
    v = 0
    for i in range(0,x):
        for j in range(0, y):
            if t[j][i] == 1:
                T(t, i, j);v+=1
    print(v)