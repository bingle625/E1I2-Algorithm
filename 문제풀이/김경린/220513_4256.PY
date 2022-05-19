

from collections import deque
from sys import stdin


def findTree(InStart, InEnd, postOrder):
    if preOrder:
        root = preOrder.popleft()
        postOrder.append(root)
        rootPre = inOrder.index(root)
        if InStart <= rootPre-1:
            findTree(InStart, rootPre-1, postOrder)
        
        if rootPre + 1 <= InEnd:
            findTree(rootPre + 1, InEnd, postOrder)
        else:
            print(postOrder.pop(), end = ' ')
            return
        
        print(postOrder.pop(), end = ' ')
    


case = int(stdin.readline().rstrip())

while case:
    postOrder = deque()

    nodeNum = int(stdin.readline().rstrip())
    preOrder = deque(map(int,stdin.readline().rstrip().split()))
    inOrder = deque(map(int, stdin.readline().rstrip().split()))
    findTree(0, len(inOrder) - 1, postOrder)
    print('')
    case -= 1
