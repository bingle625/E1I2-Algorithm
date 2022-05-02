#1620번 나는야 포켓몬 마스터 이다솜

import sys


N, M = map(int,input().split())
dic = dict()

for i in range(N):
    name = sys.stdin.readline().rstrip()
    dic[i+1] = name
    dic[name] = i+1

for i in range(M):
    ques = sys.stdin.readline().rstrip()
    if ques.isnumeric():
        print(dic[int(ques)])
    else:
        print(dic[ques])
        