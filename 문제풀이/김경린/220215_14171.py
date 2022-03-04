import collections
from sys import stdin

cities = collections.defaultdict(list)
case = int(stdin.readline())
cnt = 0

for i in range(case):
    city,state = stdin.readline().split()
    city = city[0:2]
    #cities = {
    # city :[state1,state2]
    # }

    if state in cities:
        for t_state in cities[state]:
            if city == t_state and state != city : 
                cnt += cities[state].count(city)
                break

    if state!=city:        
        cities[city].append(state)

print(cnt)