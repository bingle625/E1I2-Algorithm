# bfs, dfs, 플로이드-워셜 3가지 방식으로 풀어보기



from collections import defaultdict, deque
from operator import truediv


n = int(input())

v = []
for i in range(n):
    v_ = list(map(int, input().split()))
    v.append(v_)



def dfs(i, visited):
    for j in range(n):
        if not visited[j] and v[i][j] == 1:
            visited[j] = 1
            dfs(j, visited)
    
for i in range(n):
    visited = [ 0 for _ in range(n)]
    dfs(i, visited)
    for j in range(n):
        print(visited[j], end=' ')
    print('')


# def bfs():
#     for i in range(n):
#         visited = [ 0 for _ in range(n)]
#         visited_deque = deque()
#         for j in range(n):
#             if v[i][j] == 1 and not visited[j]:
#                 visited[j] = 1
#                 visited_deque.append(j)
        
#         while len(visited_deque):
#             node = visited_deque.popleft()
#             for j in range(n):
#                 if v[node][j] == 1 and not visited[j]:
#                     visited[j] = 1
#                     v[i][j] = 1
#                     visited_deque.append(j)
#         for j in range(n):
#             print(visited[j], end=' ')
#         print('')
    

# bfs()


# def pulid():
    # for k in range(n):
    #     for i in range(n):
    #         for j in range(n):
    #             if v[i][k] and v[k][j]:
    #                 v[i][j] = 1

    # for i in range(n):
    #     for j in range(n):
    #         print(v[i][j], end=' ')
    #     print('')
