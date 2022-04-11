# 9012번 괄호

import sys


number = int(input())

for _ in range(number):
    chars = list(sys.stdin.readline().rstrip())
    
    buff  = 0
    for char in chars:
        if char == '(':
            buff += 1
        elif char == ')' and buff > 0:
            buff += -1
        else:
            buff = -1
            break
            
    if buff == 0:
        print("YES")
    else:
        print("NO")