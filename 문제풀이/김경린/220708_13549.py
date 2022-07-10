from collections import deque
from sys import stdin

def isRightRange(num):
    if num>=0 and num<=100000:
        return True
    else:
        return False

def moveTwice(location, num):
    if num*2> target and num*2-target> target - num:
        return 0
    if isRightRange(num*2) and visited[num*2]==-1:
        visited[num*2] = visited[num]
        if num*2==target:
            print(visited[num*2])
            exit()
        location.append(num*2)
        moveTwice(location, num*2)


start, target = map(int, stdin.readline().split())

location = deque()
location.append(start)
visited = [-1 for _ in range(100001)]
visited[start] = 0

if start == target or start*2 == target:
    print(0)

else:
    while len(location):
        cur = location.popleft()
        moveTwice(location, cur)
        if isRightRange(cur+1) and visited[cur+1]==-1:
            visited[cur+1] = visited[cur] + 1
            if cur+1==target:
                print(visited[cur+1])
                break
            location.append(cur+1)
            moveTwice(location, cur+1)
        if isRightRange(cur-1) and visited[cur-1]==-1:
            visited[cur-1] = visited[cur] + 1
            if cur-1==target:
                print(visited[cur-1])
                break
            location.append(cur-1)
            moveTwice(location, cur-1)
            
    
