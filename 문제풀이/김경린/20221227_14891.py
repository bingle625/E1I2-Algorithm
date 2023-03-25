import copy
from sys import stdin
origin = []
for i in range(4):
    wheel = stdin.readline().rstrip()
    origin.append(wheel)

n = int(stdin.readline())

def turn(idx, dir):
    if dir == 1:
        wheels[idx] = wheels[idx][-1] + wheels[idx][:-1]
    else:
        wheels[idx] = wheels[idx][1:] + wheels[idx][0]

for i in range(n):
    wheels = copy.deepcopy(origin)
    wheel_num, dir = map(int, stdin.readline().split())
    if wheel_num == 1:
        turn(wheel_num-1, dir)
        while wheel_num < 4:
            if origin[wheel_num-1][2] != origin[wheel_num][-2]:
                turn(wheel_num, -dir)
                wheel_num += 1
                dir = -dir
            else:
                break 
    elif wheel_num == 4:
        turn(wheel_num-1, dir)
        while wheel_num > 1:
            if origin[wheel_num-1][-2] != origin[wheel_num-2][2]:
                turn(wheel_num-2, -dir)
                wheel_num -= 1
                dir = -dir
            else:
                break 
    else:
        tmp = wheel_num
        origin_dir = dir
        turn(tmp-1, dir)
        while tmp > 1:
            if origin[tmp-1][-2] != origin[tmp-2][2]:
                turn(tmp-2, -dir)
                tmp -= 1
                dir = -dir
            else:
                break 
        tmp = wheel_num
        dir = origin_dir
        while tmp < 4:
            if origin[tmp-1][2] != origin[tmp][-2]:
                turn(tmp, -dir)
                tmp += 1
                dir = -dir
            else:
                break 
    origin = copy.deepcopy(wheels)


score = 1
sum = 0
for i in range(4):
    if wheels[i][0] == '1':
        sum += score
    score *= 2

print(sum) 


