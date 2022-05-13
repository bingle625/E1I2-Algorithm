from collections import defaultdict
from sys import stdin

# strs = []

# strs.append(input())
# strs.append(input())

# #strs[1]에대해 따로 생각해야함

# # 공통 부분 문자 개수,남은 문자열
# common_num = [[0,''] for i in range(len(strs[0])+1)]
# common_num[0] = [0,strs[1][:]]

# for i in range(1,len(common_num)):
#     max_num = -sys.maxsize
#     if i==1:
#         for j in range(len(strs[1])):
#             if strs[1][j] == strs[0][i-1]:
#                 common_num[1][0] = 1
#                 common_num[1][1] = strs[1][j+1:]
#                 break
#     else: 
#         for j in range(0,i):
#             if common_num[j][0]>=max_num:
#                 for k in range(len(common_num[j][1])):
#                     if common_num[j][1][k] == strs[0][i-1]:
#                         if common_num[j][0]==max_num:
#                             if len(common_num[j][1])>len(common_num[i][1]):
#                                 max_num = common_num[j][0]
#                                 common_num[i][0] = common_num[j][0] + 1
#                                 common_num[i][1] = common_num[j][1][k+1:]
#                         else:
#                             max_num = common_num[j][0]
#                             common_num[i][0] = common_num[j][0] + 1
#                             common_num[i][1] = common_num[j][1][k+1:]
                                

#                         break
            

# nums = [common_num[i][0] for i in range(len(common_num))]
# print(max(nums))

str1 = list(stdin.readline().rstrip())
str2 = list(stdin.readline().rstrip())


dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
    
        if str2[i-1] == str1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])



