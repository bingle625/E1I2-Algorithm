# 11723번 집합

import sys


number = int(input())

S = set()

for i in range(number):

    cmd = list(sys.stdin.readline().rstrip().split())
    if(len(cmd) == 1):
        pass
    else:
        cmd[1] = int(cmd[1])

    if cmd[0] == 'add':
        S.add(cmd[1])
    elif cmd[0] == 'remove':
        try:
            S.remove(cmd[1])
        except:
            pass
    elif cmd[0] == 'check':
        if cmd[1] in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        try:
            S.remove(cmd[1])
        except:
            S.add(cmd[1])
    elif cmd[0] == "all":
        S = {x for x in range(1, 21)}
    else:
        S = set()
