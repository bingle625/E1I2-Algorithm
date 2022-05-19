from sys import stdin
import sys

cnt = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
signs = list(map(int,stdin.readline().split()))

max_result = -sys.maxsize
min_result = sys.maxsize


def dfs(result,i,plus,minus,multi,divide):
    global max_result, min_result

    if i == cnt:
        max_result = max(result, max_result)
        min_result = min(result, min_result)
        return
    if plus > 0:
        dfs(result + nums[i], i+1, plus-1, minus, multi, divide)
    if minus > 0:
        dfs(result - nums[i], i+1, plus, minus-1, multi, divide)
    if multi > 0:
        dfs(result * nums[i], i+1, plus, minus, multi-1, divide)
    if divide > 0:
        dfs(int(result / nums[i]), i+1, plus, minus, multi, divide-1)

dfs(nums[0],1,signs[0],signs[1],signs[2],signs[3])

print(max_result)
print(min_result)

