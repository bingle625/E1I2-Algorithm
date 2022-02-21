import collections
cities = collections.defaultdict(list)
case = int(input())
cnt = 0

for i in range(case):
    city,state = input().split()
    city = city[0:2]

    if state in cities:
        for t_state in cities[state]:
            if city == t_state and state != city:
                cnt += cities[state].count(city)
        

    cities[city].append(state)

print(cnt)