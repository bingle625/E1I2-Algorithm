

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
min_dp = sys.maxsize


dp = [ [ 0 for _ in range(case_num+1)] for _ in range(case_num+1)]
path = [ [ [] for _ in range(case_num+1)] for _ in range(case_num+1)]

for a in range(case_num+1):
    for b in range(case_num+1):
        if a==b:
            continue
        elif a>b:
            if a-b==1 and a>1:
                min_dp_a = sys.maxsize
                for i in range(0,a-1):
                    now = dp[i][b]+dist(case[i-1] if i>0 else police[0],case[a-1])
                    if now < min_dp_a:
                        dp[a][b] = now
                        min_dp_a = now
                        path[a][b] = [i,b]
                    elif now==min_dp_a:
                        if dist(case[i-1] if i>0 else police[0],case[a-1])<dist(case[path[a][b][0]-1] if path[a][b][0]>0 else police[0],case[a-1]):
                            dp[a][b] = now
                            min_dp_a = now
                            path[a][b] = [i,b]
            else:
                dp[a][b] = dp[a-1][b] + dist(case[a-2] if a>1 else police[0],case[a-1])
                path[a][b] = [a-1,b]

            if a==case_num:
                if dp[a][b]<min_dp:
                    min_dp = dp[a][b]
                    min_a = a
                    min_b = b
        elif a<b:
            if b-a==1 and b>1:
                min_dp_b = sys.maxsize
                for i in range(0,b-1):
                    now = dp[a][i]+dist(case[i-1] if i>0 else police[1],case[b-1])
                    if now < min_dp_b:
                        dp[a][b] = now
                        min_dp_b = now
                        path[a][b] = [a,i]
                    elif now==min_dp_b:
                        if dist(case[i-1] if i>0 else police[1],case[b-1])<dist(case[path[a][b][1]-1] if path[a][b][1]>0 else police[1],case[b-1]):
                            dp[a][b] = now
                            min_dp_b = now
                            path[a][b] = [a,i]
            else:
                dp[a][b] = dp[a][b-1] + dist(case[b-2] if b>1 else police[1],case[b-1])
                path[a][b] = [a,b-1]
            if b==case_num:
                if dp[a][b]<min_dp:
                    min_dp = dp[a][b]
                    min_a = a
                    min_b = b

print(dp[min_a][min_b])

go = []


while not (min_a==0 and min_b==0):
    if min_a>min_b:
        go.append(1)
    else:
        go.append(2)
    min_a,min_b = path[min_a][min_b]



for i in range(len(go)-1,-1,-1):
    print(go[i])
            





