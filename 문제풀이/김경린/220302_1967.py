
from collections import defaultdict
import sys 
sys.setrecursionlimit(10**5)

class TreeNode:

    def __init__(self,val,weight=0):
        self.val = val
        self.weight = weight
        self.child = defaultdict()   #key는 자식노드 val는 간선 가중치인 dict
node_num = int(input())

tree = []
for i in range(1,node_num+1):
    tree.append(TreeNode(i))    #트리 초기화

for i in range(node_num-1):
    parent ,child, weight = map(int,input().split())
    (tree[parent-1].child)[child] = weight #child에 추가 ex)1 2 3이면 tree[0] 노드에 child = {2:3}

#max가 될 수 있는 경우 두 가지 비교
# root에서 max인 경우, 자식들이 root가 되어 max인 경우
global child_max
child_max = 0

def dfs(node:TreeNode):
    global child_max

    max_1 = 0
    max_2 = 0
    if len(node.child)>0:
        for child_node in node.child:
            bfnode_weight = dfs(tree[child_node-1])
            node.child[child_node] += bfnode_weight
            if node.child[child_node]>max_1:
                max_2,max_1 = max_1,node.child[child_node]
            else:
                max_2 = max(max_2,node.child[child_node])
        
        node.weight = max_1 + max_2
        child_max = max(child_max,node.weight)
        return max_1

    else:
        return 0

ans = max(dfs(tree[0]),child_max)
print(ans)