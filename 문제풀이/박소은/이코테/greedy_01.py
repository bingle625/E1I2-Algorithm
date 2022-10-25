# p.311 01. 모험가 길드
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹
# 최대 몇 개의 모험가 그룹을 만들 수 있는가

N = int(input())    # N: 모험가의 수
scareList = list(map(int, input().split())) # 구성원의 공포도 리스트

scareList.sort()    # [1, 2, 2, 2, 3]
answer = 0

member = 0
for scare in scareList:
    if memeber 