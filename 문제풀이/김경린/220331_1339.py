
from collections import defaultdict, deque
from collections import Counter
from sys import stdin

# def get_idx(str,compare_str):
#     for i in range(len(str)):
#         if str[len(str)-i-1]==compare_str:
#             return len(str)-i-1


# def get_max_str(strs):
#     max_strs = []
#     max_str = max(strs,key=len)
#     for idx,str in enumerate(strs):
#         if len(str)==len(max_str):
#             max_strs.append(str)
#     if len(max_strs)>1:
#         for i in range(len(max_strs)):
#             compare_str = max_strs[i][0]
#             for j in range(len(strs)):
#                 if compare_str in strs[j]:
            

#         return max_strs[0] 
#     else:
#         return max_strs


alpha = defaultdict(int)
num = 9
str_num = int(stdin.readline())
origin = []
max_len = 0
strs = defaultdict(list)
for i in range(str_num):
    str_ = str(stdin.readline().strip())
    origin.append(str_)

    
    for i in range(0,len(str_)):
        alpha[str_[i]] += 10**(len(str_)-i)


alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
alpha_weight = defaultdict(int)
for i in alpha:
    alpha_weight[i[0]] = num
    num -= 1

for idx in range(len(origin)):
    for key in alpha_weight:
        origin[idx] = origin[idx].replace(key,str(alpha_weight[key]))


        
sum = 0

for num in origin:
    sum += int(num)

print(sum)


