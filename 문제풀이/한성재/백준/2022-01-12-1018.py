# 1018번

# 비교 함수
def countDiff(str1: str, even: bool) -> int:
    count = 0
    case1 = "WBWBWBWB"
    case2 = "BWBWBWBW"
    if(even):
        for i in range(8):
            if str1[i] != case1[i]:
                count += 1
    else:
        for i in range(8):
            if str1[i] != case2[i]:
                count += 1

    return count

# 1 입력 받기


heigt, width = input().split()
heigt = int(heigt)
width = int(width)
graph = [input() for _ in range(heigt)]
mini = 64

# 구현부
for high in range(heigt - 7):
    for wide in range(width - 7):
        sum_1 = 0
        sum_2 = 0

        for i in range(high, high+8):
            sum_1 += countDiff(graph[i][wide:wide+8], i % 2)
            sum_2 += countDiff(graph[i][wide:wide+8], (i+1) % 2)
        sum = min(sum_1, sum_2)

        if sum <= mini:
            mini = sum


print(mini)
