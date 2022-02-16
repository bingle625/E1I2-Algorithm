# 14171번
# Cities and States

import collections
from filecmp import dircmp
from sys import stdin


num = int(stdin.readline())

city = {}
used = {}
city_states = []
pairs = 0

for _ in range(num):
    inp = stdin.readline().split()
    city_state = inp[0][0:2] + inp[1]
    city_states.append(city_state)

dict = collections.Counter(city_states)

for key1 in dict.keys():
    key2 = key1[2:4] + key1[0:2]
    if key2 in dict:
        if key2 in used:
            continue
        elif key1 == key2:
            continue
        else:
            pairs += dict.get(key1) * dict.get(key2)
            used[key1] = True

# 된다고 생각했지만 안되는 것:
# 안된다고 생각했지만 되는 것:
# print(dict)
# print(used)
print(pairs)
