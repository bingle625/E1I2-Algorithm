# 시간초과
# for문 최대한 줄이기
# if i in nums
# 그냥 fraction import하면 됨...개고생

from fractions import Fraction


def to_fraction(nums):
    if "." in nums:  # 소수일 때
        nums = nums.split("0.")[1]
        if "(" in nums:
            nums = nums.replace("(", " ").replace(
                ')', " ").split()  # ( 와 )를 공백1으로 변환하고 split
            if len(nums) > 1:
                parent = int("9"*len(nums[1])+"0"*len(nums[0]))
                son = int(nums[0]+nums[1])-int(nums[0])
            else:
                parent = int("9"*len(nums[0]))
                son = int(nums[0])

        else:
            parent = int(10**len(nums))
            son = int(nums)
        print(Fraction(son, parent))


cnt = int(input())
for i in range(cnt):
    num = input()
    to_fraction(num)
