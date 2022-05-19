#3190번 뱀

import collections
import queue
from sys import stdin


N = int(input())
K = int(input())

apple = collections.defaultdict(int)
comand = collections.deque([])
track = collections.deque([])

for _ in range(K):
    y, x = map(int,stdin.readline().strip().split())
    apple[(x-1,y-1)] = 0

L = int(input())
angle = 0

for _ in range(L):
    sec, lr = stdin.readline().strip().split()
    sec = int(sec)
    lr = 90 if lr == 'L' else (-90)
    comand.append((sec,lr))

i=0 
cur = (0,0)
next_com = comand.popleft()

while True:
    i += 1
    

         
    if angle == 0 :
        cur = (cur[0]+1, cur[1])
    elif angle == 90:
        cur = (cur[0], cur[1]+1)
    elif angle == 180:
        cur = (cur[0]-1, cur[1])
    else:
        cur = (cur[0], cur[1]-1)
    
    if cur in track:
        break
    
    if cur[0] >= N or cur[0] < 0:
        break
    
    if cur[1] >= N or cur[1] < 0:
        break

    track.append((cur[0],cur[1]))
    
    
    if cur in apple:
        pass
    else:
        track.popleft()
    
    if i == next_com[0]:
        angle = (angle + next_com[1]) % 360
        if comand:
            next_com =comand.popleft()

print(i)