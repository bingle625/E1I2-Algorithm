from collections import deque

def solution(places):
    answer = []
    
    def keep_distance(place):
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    if bfs(place, y, x) == 0:
                        return 0
        return 1
    
    def bfs(place, y, x):

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        
        visited = [[0 for _ in range(5)] for _ in range(5)]
        stack = deque()
        stack.append((x, y))
        visited[y][x] = 1
        while len(stack):
            x, y = stack.popleft()
            if visited[y][x] == 3:
                continue
            else:
                for i in range(4):
                    next_x, next_y = x + dx[i], y + dy[i]
                    if 0 <= next_x < 5 and 0 <= next_y < 5 and not visited[next_y][next_x]  and place[next_y][next_x] != 'X':
                        if place[next_y][next_x] == 'P':
                            return 0
                        else:
                            visited[next_y][next_x] = visited[y][x] + 1
                            stack.append((x+dx[i], y+dy[i]))
        return 1
    
    
    
    for place in places:
        if keep_distance(place) == 0:
            answer.append(0)
        else:
            answer.append(1)
                        
    return answer


 
# 프로그래머스    
# bfs로 간 다음 거리가 2이상이면 더이상 탐색 금지, 그 중 P가 있으면 return 1