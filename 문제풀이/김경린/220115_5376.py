
def get_divisor(num):
    divisor = []
    for i in range(1, num+1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def to_fraction(nums):
    if "." in nums:  # 소수일 때
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
        parent_divisor = get_divisor(parent)
        if parent > son:
            for i in son_divisor[::-1]:
                if i in parent_divisor:
                    parent /= i
                    son /= i
                    break
        print(str(int(son))+"/"+str(int(parent)))


cnt = int(input())
for i in range(cnt):
    num = input()
    to_fraction(num)
