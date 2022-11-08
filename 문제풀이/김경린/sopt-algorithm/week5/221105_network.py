
def solution(n, computers):
    stack = []
    visited = [0 for _ in range(n)]
    cnt = 0
    for node in range(n):
        if visited[node] == 0:
            visited[node] = 1
            stack.append(node)
            cnt += 1
        while len(stack):
            cur = stack.pop()
            for i in range(n):
                if computers[cur][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
        
        
    return cnt