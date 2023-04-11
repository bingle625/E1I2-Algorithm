from collections import defaultdict, deque


n = int(input().rstrip())

target_a, target_b = map(int, input().split())

relation_num = int(input().rstrip())
relations = defaultdict(list)
visited = [0 for _ in range(n+1)]

for i in range(relation_num):
    parent, child = map(int, input().split())
    relations[parent].append(child)
    relations[child].append(parent)

tmp = deque()
visited[target_a] = 1
for child in relations[target_a]:
    tmp.append(child)
    visited[child] = 1

def bfs():
    while len(tmp):
        parent = tmp.popleft()
        for child in relations[parent]:
            if visited[child] == 0:
                tmp.append(child)
                visited[child] = visited[parent] + 1
                if child == target_b:
                    return 0
        
    

bfs()
if visited[target_b]>0:
    print(visited[target_b])
else:
    print(-1)
