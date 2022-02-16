# 14171번
# Cities and States

from sys import stdin


num = int(stdin.readline())

city = []
state_code = []
city_parsed = []
pairs = 0

for _ in range(num):
    inp = stdin.readline().split()
    city.append(inp[0])
    city_parsed.append(inp[0][0:2])
    state_code.append(inp[1])

for idx in range(len(city)):
    for idx2 in range(len(state_code)):
        if city_parsed[idx] == state_code[idx2]:
            if city_parsed[idx2] == state_code[idx]:

                # 배열로 할 경우 인덱스 중복 문제에서 벗어나기가 어려움.

                # for val in city_state_dic.values():
                #     for key in city_state_dic.keys():
                #         if val == key[0:2]:
                #             if city_state_dic.get(key)

print(pairs)
