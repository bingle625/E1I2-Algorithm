# from collections import defaultdict


# num = int(input())

# target = list(map(int,input().split(" ")))
# mix = list(map(int,input().split(" ")))

# start_dict = defaultdict(list)
# for i in range(num):
#     start_dict[i%3].append(i)

# target_dict = defaultdict(list)
# for i in range(num):
#     target_dict[target[i]].append(i)

# def compare_dict(a, b):
#     for i in range(3):
#         if sorted(a[i]) != sorted(b[i]):
#             return False
#     return True

# def make_dict(list_a):
#     new_dict = defaultdict(list)
#     for i in range(len(list_a)):
#         new_dict[i%3].append(list_a[i])
#     return new_dict

# def min_mix(start_dict, nums):
#     global target_dict
#     cnt = 0
#     while True:
#         new_nums = [ 0 for _ in range(num)]
#         for i in range(num):
#             new_nums[mix[i]] = nums[i]
#         cnt += 1
#         new_dict = make_dict(new_nums)
#         if compare_dict(new_dict, target_dict):
#             return cnt
#         elif compare_dict(new_dict, start_dict):
#             return -1

#         nums = new_nums

# if compare_dict(start_dict, target_dict):
#     print('0')
# else: 
#     print(min_mix(start_dict, [ i for i in range(num)]))




from copy import deepcopy


num = int(input())
target = []
for i in range(num):
    target.append(i%3)


nums = list(map(int,input().split(" ")))
start = deepcopy(nums)

mix = list(map(int,input().split(" ")))

cnt = 0
new_nums = [0 for _ in range(num)]
while target != nums:
    for i in range(num):
        new_nums[mix[i]] = nums[i]
    if start == new_nums:
        cnt = -1
        break
    cnt += 1
    nums = deepcopy(new_nums)
print(cnt)