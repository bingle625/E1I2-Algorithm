
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
    str_ = str(stdin.readline())
    origin.append(str_)

    str_ = deque(str_)


    max_len = max(max_len,len(str_))
    while len(str_):
        c = str_.popleft()
        strs[len(str_)+1].append(c)



for key in range(max_len,0,-1):
    if len(strs[key])>1:
        for val in strs[key]:
            if alpha[val] != 0:
                strs[key].remove(val)
        if len(strs[key])>1:
            more_weight = False
            for k in range(key-1,0,-1):
                for compare_key in strs[key]:
                    if compare_key in strs[k]:
                        if alpha[val]==0:
                            alpha[compare_key] = num
                            num -= 1
                        
            # 나머지 알파벳의 가중치가 똑같을 때
            for k in strs[key]:
                if alpha[k]==0:
                    alpha[k] = num
                    num -= 1
        else:
            if alpha[strs[key][0]]==0:
                alpha[strs[key][0]] = num
                num -= 1

        
    else:
        if alpha[strs[key][0]] == 0:
            alpha[strs[key][0]] = num
            num -= 1


for idx in range(len(origin)):
    for key in alpha:
        origin[idx] = origin[idx].replace(key,str(alpha[key]))

sum = 0

for num in origin:
    sum += int(num)

print(sum)