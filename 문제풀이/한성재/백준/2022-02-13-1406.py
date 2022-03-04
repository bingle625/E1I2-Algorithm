from sys import stdin
stackRight = []

init_str = stdin.readline()

stackLeft = list(init_str)
stackLeft.pop()
# num = int(stdin.readline())
num = int(input())

for _ in range(num):
    command = stdin.readline().split()

    if command[0] == "L":
        if len(stackLeft) != 0:
            stackRight.append(stackLeft.pop())
    elif command[0] == "D":
        if len(stackRight) != 0:
            stackLeft.append(stackRight.pop())
    elif command[0] == "B":
        if len(stackLeft) != 0:
            stackLeft.pop()
    else:
        stackLeft.append(command[1])

while len(stackRight) != 0:
    stackLeft.append(stackRight.pop())

print("".join(stackLeft))
