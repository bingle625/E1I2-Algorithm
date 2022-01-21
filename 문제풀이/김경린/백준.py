# 개인적인 백준 문제 풀이

# 1546번
# def score_avg(scores):
#     max_score = max(scores)
#     for i in range(len(scores)):
#         scores[i] = scores[i]/max_score*100
#     return sum(scores)/len(scores)


# case = int(input())
# scores = list(map(int, input().split()))

# print(score_avg(scores))


# 2839

# def num_of_bag(weight):
#     cnt = 0
#     five_num = weight//5
#     while True:
#         tmp = weight - five_num*5
#         cnt = five_num
#         if tmp % 3 == 0:
#             cnt += tmp//3
#             return cnt
#         else:
#             five_num -= 1
#             if five_num < 0:
#                 return -1


# weight = int(input())
# print(num_of_bag(weight))

# 4673번

# def self_num():
#     all_num = range(10000)
#     d = []
#     for i in range(10000):
#         tmp = str(i)
#         sum_i = i
#         for j in tmp:
#             sum_i += int(j)

#         if sum_i < 10000:
#             d.append(sum_i)
#     d_c = [x for x in all_num if x not in d]

#     for i in d_c:
#         print(i)


# self_num()

# 2750번

# def up_sort(nums):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]

#     for i in nums:
#         print(i)


# nums = []
# cnt = int(input())
# for i in range(cnt):
#     tmp = int(input())
#     nums.append(tmp)

# up_sort(nums)

# 2941번
def cnt_alpha(strs):
    alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    cnt = 0
    for i in alpha:
        if i in strs:
            strs = strs.replace(i, '0')

    print(len(strs))


strs = input()
cnt_alpha(strs)
