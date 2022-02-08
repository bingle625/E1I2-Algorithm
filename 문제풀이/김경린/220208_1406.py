

strs = list(input())
cursor = len(strs)

num = int(input())

for i in range(num):
    command = list(map(str, input().split()))
    if len(command) > 1:
        if command[0] == 'P':
            strs.insert(cursor, command[1])
            cursor += 1
    else:
        if command[0] == 'L':
            if cursor > 0:
                cursor -= 1
        elif command[0] == 'D':
            if cursor < len(strs):
                cursor += 1
        elif command[0] == 'B':
            if cursor > 0:
                cursor -= 1
                strs.pop(cursor)

for i in strs:
    print(i, end='')
