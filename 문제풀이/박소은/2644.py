# 최단경로 문제 -> BFS
from collections import deque, defaultdict

def BFS(root):
    visited = [root]
    queue = deque([(root, 0)])
    
    while queue:
        v = queue.popleft()
        for w in relations[v[0]]:
            if w == target2:
                return v[1]+1
            
            if w not in visited:
                visited.append(w)
                queue.append((w, v[1]+1))
    
    return -1

n = int(input())
target1, target2 = map(int, input().split())
m = int(input())    # m: 관계의 개수

relations = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

print(BFS(target1))