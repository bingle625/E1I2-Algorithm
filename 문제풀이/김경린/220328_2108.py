from collections import Counter
from sys import stdin

# def quicksort(A,lo,hi):
#     def partition(lo,hi):
#         pivot = A[hi]
#         left = lo
#         for right in range(lo,hi):
#             if A[right] < pivot:
#                 A[left],A[right] = A[right],A[left]
#                 left += 1
#         A[left],A[hi] = A[hi],A[left]
#         return left
    
#     if lo < hi:
#         pivot = partition(lo,hi)
#         quicksort(A,lo,pivot-1)
#         quicksort(A,pivot+1,hi)


N = int(stdin.readline())
nums = []
for i in range(N):
    num = int(stdin.readline())
    nums.append(num)

nums.sort()

print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])

nums_cnt = Counter(nums)
cnt_tuple = nums_cnt.most_common()
if len(cnt_tuple)>1:
    if cnt_tuple[0][1]==cnt_tuple[1][1]:
        print(cnt_tuple[1][0])
    else:
        print(cnt_tuple[0][0])
else:
    print(cnt_tuple[0][0])
print(nums[len(nums)-1]-nums[0])