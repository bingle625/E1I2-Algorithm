
from collections import deque
from sys import stdin
from collections import defaultdict

class TreeNode(object):
    parent = 0
    child = []
    def __init__(self, val=0):
        self.val = val

num = int(stdin.readline())
tree = defaultdict(deque)

node = []
for i in range(1,num+1):
    node.append(TreeNode(i))



for i in range(num-1):
    val1,val2 = map(int,stdin.readline().split())
    tree[val1].append(val2)
    tree[val2].append(val1)


root = deque()
root.append(node[0])

def bfs():
    while root:
        root_node = root.popleft()
        root_val = root_node.val
        
        while len(tree[root_val]):
            val = tree[root_val].popleft()
            root_node.child.append(node[val-1])
            node[val-1].parent = root_val
            root.append(node[val-1])
            tree[val].remove(root_val)


bfs()

root = deque()
root.append(node[0])

for i in range(2,num+1):
    print(node[i-1].parent)