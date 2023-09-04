from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split(' '))
bridges = defaultdict(list)

for i in range(m):
	s, e = map(int, input().split(' '))
	bridges[s].append(e)

visited = [0 for _ in range(n+1)]
def dfs(cur, visited):
	for bridge in bridges[cur]:
		if not visited[bridge]:
			if cur in bridges[bridge]:
				visited[bridge] = 1
				dfs(bridge, visited)
	return
	
cnt = 0

for i in range(1,n+1):
	if not visited[i]:
		visited[i] = 1
		dfs(i, visited)
		cnt += 1
		
	

print(cnt)
	