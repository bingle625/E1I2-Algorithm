from collections import defaultdict, deque

n, m, s, e = map(int, input().split(' '))
graph = defaultdict(list)
for i in range(m):
	tmp1, tmp2 = map(int, input().split(' '))
	graph[tmp1].append(tmp2)
	graph[tmp2].append(tmp1)

def bfs(ban):
	deq = deque()
	visited = [0 for _ in range(n+1)]
	visited[s] = 1
	visited[ban] = 1
	deq.append((s, 1))
	while len(deq):
		node, depth = deq.popleft()
		if node == e:
			return depth
		for next_node in graph[node]:
			if not visited[next_node]:
				deq.append((next_node, depth+1))
				visited[next_node] = 1
	return -1

for i in range(1, n+1):
	if i == s or i == e:
		print(-1)
	else:
		print(bfs(i))
	