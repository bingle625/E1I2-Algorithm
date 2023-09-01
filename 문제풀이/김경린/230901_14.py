from collections import defaultdict, deque

n, m, start = map(int, input().split(' '))
graph = defaultdict(list)
for i in range(m):
	node1, node2 = map(int, input().split(' '))
	graph[node1].append(node2)
	graph[node2].append(node1)

for key in graph.keys():
	graph[key].sort()
	graph[key] = deque(graph[key])
	
def find():
	visited = [0 for _ in range(n+1)]
	cur_node = start
	cnt = 1
	while len(graph[cur_node]) > 0:
		visited[cur_node] = 1
		is_exist = False
		for next_node in graph[cur_node]:
			if visited[next_node] == 0:
				cur_node = next_node
				is_exist = True
				break
		if is_exist == False:
			print(cnt, end=' ')
			print(cur_node)
			return 0
		cnt += 1
	print(cnt, end=' ')
	print(cur_node)
	return 0
find()

