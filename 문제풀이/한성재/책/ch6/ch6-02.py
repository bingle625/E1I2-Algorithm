# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         new_arr = []
#         while len(s) != 0:
#             new_arr.append(s.pop())

#         s = new_arr[:]
# 왜 안되는 답일까 이건? return 자체가 [] 공 스트링으로 나옴
