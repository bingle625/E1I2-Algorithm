from collections import defaultdict, deque
from sys import stdin


cityNum, roadNum, k, start = map(int, stdin.readline().split(' '))
graph = defaultdict(deque)
visited = [0 for _ in range(cityNum+1)]

visited[start] = 1

citys = deque()
citys.append(start)

answer = []
for i in range(roadNum):
    s, d = map(int,  stdin.readline().split())
    graph[s].append(d)

def bfs():
    while len(citys):
        city = citys.popleft()
        for goCity in graph[city]:
            if visited[goCity]==0:
                visited[goCity] = visited[city] + 1
                if visited[goCity]== k+1:
                    answer.append(goCity)
                elif visited[goCity]>k+1:
                    break
                citys.append(goCity)
bfs()
answer.sort()
if answer:
    for city in answer:
        print(city)
else:
    print(-1)