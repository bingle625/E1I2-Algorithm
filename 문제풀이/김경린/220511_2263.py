from collections import defaultdict, deque
from sys import stdin
import sys
sys.setrecursionlimit(10**9)


nodeNum = int(stdin.readline())
inOrder = list(map(int, stdin.readline().split()))
postOrder = list(map(int, stdin.readline().split()))

pos = [0]*(nodeNum+1)
for i in range(nodeNum): 
    pos[inOrder[i]] = i



def findTree(inOrderStart,inOrderEnd,postOrderStart,postOrderEnd):

    parent = postOrder[postOrderEnd]
    parentIdx = pos[parent] - inOrderStart #상대적으로 계산
    print(parent, end = ' ')

    # leftIn = inOrder[0:parentIdx]
    # leftPost = postOrder[0:parentIdx]

    if inOrderStart <= inOrderStart+parentIdx-1:
        if inOrderStart == inOrderStart+parentIdx-1:
            print(inOrder[inOrderStart], end = ' ')
        else:
            findTree(inOrderStart, inOrderStart+parentIdx-1, postOrderStart, postOrderStart+parentIdx-1)


    # rightIn = inOrder[parentIdx+1:]
    # rightPost = postOrder[parentIdx:-1]
    if  inOrderStart+parentIdx + 1 <= inOrderEnd:
        if inOrderStart+parentIdx + 1 == inOrderEnd:
            print(inOrder[inOrderEnd], end = ' ')

        else:
            findTree(inOrderStart+parentIdx + 1, inOrderEnd, postOrderStart+parentIdx, postOrderEnd - 1)
    
findTree(0, len(inOrder)-1, 0,len(postOrder)-1)

