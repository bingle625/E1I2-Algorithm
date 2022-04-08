

from collections import deque
import sys

def dist(pos1,pos2):
    x1,y1 = pos1[0],pos1[1]
    x2,y2 = pos2[0],pos2[1]

    return abs(x1-x2) + abs(y1-y2)

num = int(input())
case_num = int(input())

case = deque()

for i in range(case_num):
    x,y = map(int,input().split())
    case.append((x,y))

police = [(1,1),(num,num)]
case_police = []

dp = [ [ 0 for _ in range(case_num+1)] for _ in range(case_num+1)]

for a in range(case_num+1):
    for b in range(case_num+1):
        if a==b:
            continue
        elif a>b:
            if a-b==1 and a>1:
                dp[a][b] =  min( [dp[i][b]+dist(case[i] if i>0 else police[0],case[a-1]) for i in range(0,a-1)] ) 
            else:
                dp[a][b] = dp[a-1][b] + dist(case[a-2] if a>1 else police[0],case[a-1])
        elif a<b:
            if b-a==1 and b>1:
                dp[a][b] = min( [dp[a][i]+dist(case[i] if i>0 else police[1],case[b-1]) for i in range(0,b-1)] )  
            else:
                dp[a][b] = dp[a][b-1] + dist(case[b-2] if b>1 else police[1],case[b-1])

end = []
for x in range(case_num+1):
    for y in range(case_num+1):
        if not (x==case_num and y==case_num) and (x==case_num or y==case_num) :
            end.append(dp[x][y])
print(min(end))
    