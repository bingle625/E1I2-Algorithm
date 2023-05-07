# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 같은 간선은 한 번만 주어진다.

from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

visited = []    # 방문한 vertex 저장

def DFS(root):
    result = []
    stack = [root]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            result.append(v)
            for w in links[v]:
                stack.append(w)
    # return result

N, M = map(int, input().split())    # N: vertex#, M: link#
links = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)
answer = 0

for elem in links.keys():
    if elem not in visited:
        DFS(elem)
        answer += 1

for i in range(1, N+1):
    if not links[i]:    # 연결되어 있지 않은 독립된 vertex인 경우
        answer += 1
    elif i not in visited:  # 방문하지 않은 vertex인 경우
        DFS(elem)
        answer += 1

print(answer)