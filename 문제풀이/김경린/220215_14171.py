import collections
cities = collections.defaultdict(list)
case = int(input())
cnt = 0
for i in range(case):
    city,state = input().split()
    city = city[0:2]
    if state in cities:
        if city in cities[state]:
            cnt += 1
        

    cities[city].append(state)

print(cnt)