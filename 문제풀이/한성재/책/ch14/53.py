# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 풀이2. 반복구조로 중위 순회
class Solution(object):

    def minDiffInBST(self, root):
        prev = -sys.maxsize
        result = sys.maxsize
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result

# #풀이 1. 재귀구조로 중위 순회

# class Solution(object):
#     prev = -sys.maxsize
#     result = sys.maxsize

#     def minDiffInBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root.left:
#             self.minDiffInBST(root.left)

#         self.result = min(self.result, root.val - self.prev)
#         self.prev = root.val

#         if root.right:
#             self.minDiffInBST(root.right)

#         return self.result
