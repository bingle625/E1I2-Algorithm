# p.349 19. 연산자 끼워 넣기
# N개의 수로 이루어진 수열, 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자
# 연산자는 +, -, /, * 로 이루어져 있다.
# 만들 수 있는 식의 최소와 최대를 만들어라.

N = int(input())
array = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())

answer = []

def dfs(index, currentVal):
    global minVal, maxVal, plus, minus, multi, divide

    if index == N:
        answer.append(currentVal)
    else:
        if plus > 0:
            plus -= 1
            dfs(index+1, currentVal + array[index])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(index+1, currentVal - array[index])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(index+1, currentVal * array[index])
            multi += 1
        if divide > 0:
            divide -= 1
            dfs(index+1, int(currentVal / array[index]))
            divide += 1