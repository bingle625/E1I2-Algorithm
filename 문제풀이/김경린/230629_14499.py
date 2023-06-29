from copy import deepcopy


n, m, y, x, commands_num = map(int, input().split(' '))
#   1
# 3 0 2
#   4
#   5 
dice = [ 0 for _ in range(6)]

maps = []
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    maps.append(tmp)

commands = map(int, input().split(' '))

for c in commands:
    new_dice = [0 for _ in range(6)]
    if c==1:
        if x+1 >= m:
            continue
        x += 1
        new_dice[0] = dice[2]
        new_dice[1] = dice[1]
        new_dice[2] = dice[5]
        new_dice[3] = dice[0]
        new_dice[4] = dice[4]
        new_dice[5] = dice[3]
    elif c==2:
        if x-1 < 0:
            continue
        x -= 1
        new_dice[0] = dice[3]
        new_dice[1] = dice[1]
        new_dice[2] = dice[0]
        new_dice[3] = dice[5]
        new_dice[4] = dice[4]
        new_dice[5] = dice[2]
    elif c==3:
        if y-1 < 0:
            continue
        y -= 1
        new_dice[0] = dice[4]
        new_dice[1] = dice[0]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1]

    elif c==4:
        if y+1 >= n:
            continue
        y+=1
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
    

    dice = new_dice
    if maps[y][x] == 0:
        maps[y][x] = dice[0]
    else:
        dice[0] = maps[y][x]
        maps[y][x] = 0
    
    print(dice[-1])    

    
