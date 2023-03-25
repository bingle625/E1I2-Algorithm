from collections import defaultdict, deque
from sys import stdin

user_num, relations_num = map(int,stdin.readline().split())

relations = defaultdict(list)

bacon = [ [0 for _ in range(user_num+1)] for _ in range(user_num+1)]

for i in range(relations_num):
    a,b = map(int,stdin.readline().split())
    relations[a].append(b)
    relations[b].append(a)
    bacon[a][b] = 1
    bacon[b][a] = 1

def bfs(start, dest):
    visited_deque = deque()
    visited_deque.append(start)
    visited = [ 0 for _ in range(user_num+1)]
    visited[start] = 0
    while len(visited_deque):
        s = visited_deque.popleft()
        for neighbor in relations[s]:
            if not visited[neighbor]:
                visited_deque.append(neighbor)
                visited[neighbor] = visited[s] + 1
                if neighbor == dest:
                    return visited[neighbor]


    
def find():
    for i in range(1, user_num+1):
        for j in range(1, user_num+1):
            if i!=j:
                if not bacon[i][j]:
                    bacon[i][j] = bfs(i,j)
                    bacon[j][i] = bacon[i][j]

find()
sum_bacon = [0 for _ in range(user_num)]
for idx in range(1,user_num+1):
    sum_bacon[idx-1] = sum(bacon[idx])

print(sum_bacon.index(min(sum_bacon))+1)
                    

