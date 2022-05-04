from collections import deque
from sys import stdin
import sys
sys.setrecursionlimit(100000)

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def toPost(root):
    if root is None:
        return
    toPost(root.left)
    toPost(root.right)
    print(root.val)

preorder = deque()

while True:
    try:
        node_val = int(stdin.readline())
        node = TreeNode(node_val)
        preorder.append(node)
    except:
        break

visited = deque()

while len(preorder):
    node = preorder.popleft()
    
    if len(visited):
        if node.val<visited[-1].val:
            visited[-1].left = node
        else:
            while len(visited):
                parent = visited.pop()
                if parent.val<node.val:
                    if len(visited):
                        if visited[-1].val>node.val:
                            parent.right = node
                            break
                    else:
                        parent.right = node
                        break
    else:
        root = node


    visited.append(node)

toPost(root)