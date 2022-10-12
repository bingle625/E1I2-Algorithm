from collections import deque


instructionsNum = int(input())

deq = deque()
while instructionsNum:
    instruction = list(input().split())
    if len(instruction)>1:
        if instruction[0] == 'push':
            deq.append(instruction[1])
    else:
        if instruction[0] == 'front':
            if len(deq):
                print(deq[0])
            else:
                print(-1)
        elif instruction[0] == 'pop':
            if len(deq):
                print(deq.popleft())
            else:
                print(-1)
        elif instruction[0] == 'size':
            print(len(deq))
        elif instruction[0] == 'empty':
            if len(deq):
                print(0)
            else:
                print(1)
        elif instruction[0] == 'back':
            if len(deq):
                print(deq[-1])
            else:
                print(-1)
    instructionsNum -= 1

