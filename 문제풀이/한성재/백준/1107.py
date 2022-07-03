# 1107 리모컨

import sys

init = 100
target_num = int(sys.stdin.readline().rstrip())
broken_num = int(sys.stdin.readline().rstrip())
brokens = []
if broken_num != 0:
    brokens = list(map(int, sys.stdin.readline().rstrip().split()))

num_arr = []

for i in range(10):
    if num_arr not in brokens:
        num_arr.append(i)

step = abs(target_num - init)
target_num = list(str(target_num))

get_num = []

for char in target_num:
    num = 0
    while True:
        if int(char) - num not in brokens and int(char) - num >= 0:
            get_num.append(int(char)-num)
            break
        if int(char) + num not in brokens and int(char) + num <= 9:
            get_num.append(int(char)+num)
            break
        num += 1

get_num = int("".join(map(str, get_num)))
target_num = int("".join(target_num))
step = min(step, abs(target_num-get_num)+len(str(get_num)))
print(step)
