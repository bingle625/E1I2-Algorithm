# 14171번
# Cities and States

from sys import stdin


num = int(stdin.readline())

city = {}
state_code = []
city_parsed = []
pairs = 0

for _ in range(num):
    inp = stdin.readline().split()
    # city.append(inp[0])
    city_parsed.append(inp[0][0:2])
    state_code.append(inp[1])

    city[inp[0]]

    for idx in range(len(city_parsed)-1):
        if inp[0][0:2] == state_code[idx]:
            if city_parsed[idx] == inp[1]:
                pairs += 1
            else:
                continue
        else:
            continue

print(pairs)
