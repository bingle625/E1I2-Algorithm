# 단어 정렬

# 828ms
# 날먹 코드
def sort_strs(strs):
    strs = set(strs)
    strs = list(strs)
    strs.sort()
    strs.sort(key=len)

    for str in strs:
        print(str)


cnt = int(input())
strs = []
for i in range(cnt):
    tmp = input()
    strs.append(tmp)

sort_strs(strs)
