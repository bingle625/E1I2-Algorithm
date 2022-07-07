# N: 물병 개수, K: 한 번에 옮길 수 있는 물병의 수
# 같은 양의 물병 2개 골라서 한쪽으로 몰빵

N, M = map(int, input().split())
buy = 0
bottles = [1 for _ in range(N)]

while len(bottles) > M:
    if bottles[0] == bottles[1]:
        bottles.append(bottles[0] * 2)
        del bottles[0]
        del bottles[0]
    else:
        buy += 1
        bottles.insert(0, 1)
        if bottles[0] == bottles[1]:
            bottles.append(bottles[0] * 2)
            del bottles[0]
            del bottles[0]
            bottles.sort()

print(buy)