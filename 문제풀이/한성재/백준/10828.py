#10828번 스택 구현

from collections import deque
from sys import stdin


class myStack:
    def __init__(self) -> None:
        self.container = deque([])
    
    def myPush(self, number):
        self.container.append(number)
    
    def myPop(self):
        if self.container:
            print(self.container.pop())
        else:
            print(-1)
    
    def mySize(self):
        print(len(self.container))
    
    def myEmpty(self):
        if self.container:
            print(0)
        else:
            print(1)
    
    def myTop(self):
        if self.container:
            print(self.container[-1])
        else:
            print(-1)

number = int(input())

stac = myStack()

for _ in range(number):
    query = list(stdin.readline().rstrip().split())
    if len(query) == 2:
        stac.myPush(int(query[1]))
    else:
        if query[0] == "pop":
            stac.myPop()
        elif query[0] == "size":
            stac.mySize()
        elif query[0] == "empty":
            stac.myEmpty()
        elif query[0] == "top":
            stac.myTop()
        else:
            print("wrong input")