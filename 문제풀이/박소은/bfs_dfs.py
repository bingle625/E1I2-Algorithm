from collections import deque

graph = {
	1 : [2,3,4],
	2 : [5],
	3 : [5],
	4 : [],
	5 : [6,7],
	6 : [],
	7 : [3]
}

def BFS(root):
    visited = [root]    # 현재 노드 방문 처리
    queue = deque([root])
    
    while queue:
        v = queue.popleft() # 큐에서 원소 꺼내기
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited

# print(BFS(1))


def recursive_dfs(root, visited=[]):
    visited.append(root)
    
    for w in graph[root]:
        if w not in visited:
            visited = recursive_dfs(w, visited)
            
    return visited

# print(recursive_dfs(1, []))


def stack_dfs(root):
    visited = []
    stack = [root]
    
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    
    return visited

# print(stack_dfs(1))



# 섬의 개수 구하기: DFS 사용
# 11110
# 11010
# 11000
# 00000

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    
    def dfs(i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
            return
        
        grid[i][j] = 0  # 지나온 육지는 0으로 표시
        
        # 동서남북 탐색
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

print(numIslands([['1', '1', '1', '1', '0'], 
                 ['1', '1', '0', '1', '0'], 
                 ['1', '1', '0', '0', '0'], 
                 ['0', '0', '0', '0', '0']]))