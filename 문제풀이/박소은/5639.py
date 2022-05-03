from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    root: TreeNode = None
    ptr = root

    def buildTree(self, preorder: List[int]):
        root = TreeNode(preorder[0])

        for node in preorder[1:]:
            if ptr.val > node:
                ptr.left = TreeNode(node)
                ptr = ptr.left
            else:
                ptr.right = TreeNode(node)
                ptr = ptr.right

        return root

    def postorder(node: TreeNode):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        print(node.val)
        

# 입력
s = Solution()
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
root = s.buildTree(tree)
s.postorder(root)