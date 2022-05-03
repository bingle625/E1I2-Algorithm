from collections import deque
from sys import stdin
import copy

#문장의 순서만 조금 바꾼건데 시간초과가 해결,,,? 비교해보기

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N,M = map(int,stdin.readline().split())
maze = []
visited = deque()
for i in range(N):
    maze_line=stdin.readline()
    maze_line=list(maze_line)
    maze.append(maze_line)

visited.append([0,1,1])


def bfs():

    while True:
        tmp = visited.popleft()
        
        current_cnt ,current_x,current_y = tmp[0],tmp[1],tmp[2]
    
        if maze[current_y-1][current_x-1]=='1':
            current_cnt+=1
            maze[current_y-1][current_x-1]=0
            
            if current_x == M and current_y==N:
                return current_cnt

            for i in range(4):
                next_x = current_x + dx[i]
                next_y = current_y + dy[i]
                if next_x>0 and next_y>0 and next_x<M+1 and next_y<N+1  and maze[next_y-1][next_x-1]=='1':
                    visited.append([current_cnt,next_x,next_y])


                    

                    

                
                
    


print(bfs())