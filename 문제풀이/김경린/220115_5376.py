# 시간초과
# for문 최대한 줄이기
# if i in nums

import sys


def get_divisor(num):
    divisor = []
    divisor_back = []

    for i in range(1, int(num**(1/2))+1):
        if num % i == 0:
            divisor.append(i)
            if i != (num//i):
                divisor_back.append(num//i)
    return divisor+divisor_back[::-1]


def to_fraction(nums):
    if nums[0] == "0":  # 소수일 때
        nums = nums.split("0.")[1]
        if "(" in nums:
            nums = nums.replace("(", " ").replace(
                ')', " ").split()  # ( 와 )를 공백으로 변환하고 split
            if len(nums) > 1:
                parent = int("9"*len(nums[1])+"0"*len(nums[0]))
                son = int(nums[0]+nums[1])-int(nums[0])
            else:
                parent = int("9"*len(nums[0]))
                son = int(nums[0])

        else:
            parent = int(10**len(nums[0]))
            son = int(nums[0])
        son_divisor = get_divisor(son)
        for i in son_divisor[::-1]:
            if parent > i:
                if parent % i == 0:
                    parent //= i
                    son //= i
                    break

        print(str(son)+"/"+str(parent))


cnt = int(sys.stdin.readline())
for i in range(cnt):
    num = sys.stdin.readline()
    to_fraction(num)
