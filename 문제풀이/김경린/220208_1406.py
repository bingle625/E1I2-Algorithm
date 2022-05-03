

from sys import stdin

strs = list(stdin.readline().strip())
tmp = []


num = int(stdin.readline())

for i in range(num):

    command = list(map(str, stdin.readline().strip().split()))
    if len(command) > 1:
        if command[0] == 'P':
            strs.append(command[1])
    else:
        if command[0] == 'L':
            if strs:
                char = strs.pop()
                tmp.append(char)
        elif command[0] == 'D':
            if tmp:
                char = tmp.pop()
                strs.append(char)
        elif command[0] == 'B':
            if strs:
                strs.pop()


for i in strs:
    print(i, end='')

for i in range(len(tmp)):
    print(tmp.pop(), end='')
