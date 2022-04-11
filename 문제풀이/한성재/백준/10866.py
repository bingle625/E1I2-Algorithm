# 10866번 덱

#10866 덱 구현

from collections import deque
from sys import stdin


class myQueue:
    def __init__(self) -> None:
        self.container = deque([])
    
    def push_front(self, number):
        self.container.appendleft(number)

    def push_back(self, number):
        self.container.append(number)
    
    def pop_front(self):
        if self.container:
            print(self.container.popleft())
        else:
            print(-1)

    def pop_back(self):
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
    
    def myFront(self):
        if self.container:
            print(self.container[0])
        else:
            print(-1)
    
    def myBack(self):
        if self.container:
            print(self.container[-1])
        else:
            print(-1)

number = int(input())

stac = myQueue()

for _ in range(number):
    query = list(stdin.readline().rstrip().split())
    if len(query) == 2:
        if query[0] == "push_front":
            stac.push_front(int(query[1]))
        elif query[0] == "push_back":
            stac.push_back(int(query[1]))
        else:
            print("wrong query")
    else:
        if query[0] == "pop_front":
            stac.pop_front()
        elif query[0] == "pop_back":
            stac.pop_back()
        elif query[0] == "size":
            stac.mySize()
        elif query[0] == "empty":
            stac.myEmpty()
        elif query[0] == "front":
            stac.myFront()
        elif query[0] == "back":
            stac.myBack()
        else:
            print("wrong input")