

from sys import stdin

strs = list(stdin.readline())
tmp = []


num = int(stdin.readline())

for i in range(num):
    command = list(map(str, stdin.readline().split()))
    if len(command) > 1:
        if command[0] == 'P':
            strs.append(command[1])
    else:
        if command[0] == 'L':
            if len(strs) > 0:
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
