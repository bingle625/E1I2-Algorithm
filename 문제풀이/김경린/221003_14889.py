import math
from sys import stdin
players = int(stdin.readline())
ability = [[0 for _ in range(players)] for _ in range(players)]
for i in range(players):
    ability[i] = list(map(int, stdin.readline().split()))


def cal_ability(member):
    ability_sum = 0
    for i in range(len(member)):
        for j in range(i+1, len(member)):
            ability_sum += ability[member[i]][member[j]]
            ability_sum += ability[member[j]][member[i]]
    return ability_sum
# 0이 포함되는 집합과 0이 포함되지 않는 집합

cnt = 1
team = [ i for i in range(players)]
team1 = [0,0 ]
team2 = []
min_gap =  math.inf

def bfs():
    global min_gap
    while True:
        mem = team1.pop()
        if len(team1) == 0:
            break
        for i in range(mem+1,players):
            team1.append(i)
            if len(team1) == players//2:
                team1_ability = cal_ability(team1)
                team2 = list(set(team) - set(team1))
                team2_ability = cal_ability(team2)
                gap = abs(team1_ability-team2_ability)
                if gap < min_gap:
                    min_gap = gap
                team1.pop()
    



bfs()
print(min_gap)

        

    