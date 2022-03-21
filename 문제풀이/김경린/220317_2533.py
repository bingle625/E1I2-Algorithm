
from collections import defaultdict, deque
from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**9)


node_num = int(stdin.readline())

graph = [ []for _ in range(node_num+1)]
#dp[i][0]는 i노드가 얼리어답터일 때 서브 트리에서 얼리어답터의 최소값
#dp[i][1]은 i노드가 얼리어답터가 아닐 때의 서브트리에서 얼리어답터의 최소값
dp = [[0,0] for _ in range(node_num+1)]
visited = [0 for _ in range(node_num+1)]

for i in range(node_num-1):
    node_1,node_2 = map(int,stdin.readline().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)



def dfs(r):
    visited[r] = 1
    dp[r][0] = 1
    for i in graph[r]:
        if not visited[i]:
            dfs(i)
            #r이 얼리어답터이면 자식인 i는 얼리어답터인지 상관 x 따라서 min
            dp[r][0] += min(dp[i][0],dp[i][1])
            #r이 얼리어답터가 아니면 무조건 자식은 얼리어답터여야됨
            dp[r][1] += dp[i][0]

dfs(1)

print(min(dp[1][0],dp[1][1]))
                

    