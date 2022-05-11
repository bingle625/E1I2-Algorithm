from collections import defaultdict, deque
from sys import stdin

nodeNum = int(stdin.readline())
inOrder = list(map(int, stdin.readline().split()))
postOrder = list(map(int, stdin.readline().split()))



def findTree(inOrder,postOrder):

    parent = postOrder[-1]
    parentIdx = inOrder.index(parent)
    leftIn = inOrder[0:parentIdx]
    leftPost = postOrder[0:parentIdx]
    print(parent, end = ' ')

    if leftIn:
        # if len(leftIn) == 1:
        #     tree[parent].append(leftIn[0])
        # else:
            findTree(leftIn, leftPost)


    rightIn = inOrder[parentIdx+1:]
    rightPost = postOrder[parentIdx:-1]

    if rightIn:
        # if len(rightIn) == 1:
        #     tree[parent].append(rightIn[0])
        
        # else:
            findTree(rightIn,rightPost)
    
findTree(inOrder, postOrder)