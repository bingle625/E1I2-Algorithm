from collections import defaultdict, deque

num, v_num, start = map(int, input().split())

graph = defaultdict(list)

for i in range(v_num):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, num+1):
    graph[i].sort()


def dfs(visited, node):
    print(node, end=' ')
    visited[node] = 1
    for n in graph[node]:
        if not visited[n]:
            dfs(visited, n)

def bfs(visited, start):
    stack = deque()
    stack.append(start)
    visited[start] = 1
    while len(stack):
        node = stack.popleft()
        print(node, end=' ')
        for n in graph[node]:
            if not visited[n]:
                visited[n] = 1
                stack.append(n)


dfs([0 for _ in range(num+1)], start)
print('')
bfs([0 for _ in range(num+1)], start)