from sys import stdin
num, target_sum = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))


cnt = 0  
def findTarget(idx, target):
    global cnt
    for i in range(idx, len(nums)):
        if target - nums[i] == 0:
            cnt += 1
        findTarget(i+1, target-nums[i])  

findTarget(0,target_sum)
print(cnt)