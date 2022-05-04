# 단어 정렬

# 풀이1

# 828ms
# 날먹 코드
# def sort_strs(strs):
#     strs = set(strs)
#     strs = list(strs)
#     strs.sort()
#     strs.sort(key=len)

#     for str in strs:
#         print(str)


# cnt = int(input())
# strs = []
# for i in range(cnt):
#     tmp = input()
#     strs.append(tmp)

# sort_strs(strs)

# 풀이2
# c스타일로 하려했는데 시간 초과가 계속 뜸...
from sys import stdin


def sort_strs(strs):
    for i in range(len(strs)-1):
        min = strs[i]
        for j in range(i+1, len(strs)):
            if len(min) > len(strs[j]):
                strs[i], strs[j] = strs[j], strs[i]
                min = strs[i]
            elif len(min) == len(strs[j]) and min > strs[j]:
                strs[i], strs[j] = strs[j], strs[i]
                min = strs[i]
    for str in strs:
        print(str, end="")


cnt = int(stdin.readline())
strs = []
for i in range(cnt):
    tmp = stdin.readline()
    strs.append(tmp)

# 중복 제거
strs = set(strs)
strs = list(strs)

sort_strs(strs)
