import sys
input = sys.stdin.readline


N = int(input())

nums = list(map(int, input().split()))

a, b, c, d = map(int, input().split())

max_ans, min_ans = -sys.maxsize - 1, sys.maxsize


def solution(num, idx, add, sub, mul, div):
    global max_ans, min_ans
    if idx == N:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return

    if add > 0:
        solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        solution(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        solution(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)


solution(nums[0], 1, a, b, c, d)
print(max_ans)
print(min_ans)
