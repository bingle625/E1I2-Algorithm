
from collections import deque
from sys import stdin

def comparing(phone_nums:list):
    for i in range(len(phone_nums)-1):
        if phone_nums[i] ==phone_nums[i+1][:len(phone_nums[i])]:
            return "NO"
    return "YES"

        


case = int(stdin.readline())

for i in range(case):
    nums = int(stdin.readline())
    phone_nums = []
    for j in range(nums):
        phone_num = stdin.readline().strip()
        phone_nums.append(phone_num)
    
    phone_nums.sort()
    print(comparing(phone_nums))
