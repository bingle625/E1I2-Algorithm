#1261번 알고스팟 아직 풀이 X

# class solution:
    
#     def __init__(self):
#         self.N,self.M = map(int,input().split())
#         self.room = [list(map(int, input())) for _ in range(self.M)]


#     def countOne(self,x:int, y:int) -> int:
                
#         if x+1 < self.N or y+1 < self.M:
            
#             if x+1 >= self.N:
#                 return self.room[y][x] + self.countOne(x,y+1)
#             elif y+1 >= self.M:
#                 return self.room[y][x] + self.countOne(x+1,y)
#             else:
#                 return self.room[y][x] + min(self.countOne(x+1,y), self.countOne(x,y+1))
#         else:
#             return self.room[y][x]
        
        
# s = solution()

# print(s.countOne(0,0))


from collections import deque
import sys


N,M =map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(M)]

visited =[[False]*N for _ in range(M)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def scope(y,x):
    if y>=0 and y<M and x>=0 and x<N:
        return True
    else:
        return False
    
def bfs():
    q=deque()
    q.append([0,0])
    visited[0][0] = True
    
    while q:
        fy,fx = q.popleft
        if fy == M-1 and fx == N-1:
            print(graph[fy][fx])
            break
        for i in range(4):
            my = fy+dy[i]
            mx = fx+dx[i]
            
            if scope(my,mx):
                if not visited[my][mx] and graph[my][mx] ==0:
                    