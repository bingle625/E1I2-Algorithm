# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # # 풀이1 파이썬 다운 방식
        # if root:
        #     root.left, root.right =\
        #         self.invertTree(root.right), self.invertTree(root.left)
        #     return root
        # return None

        # # 풀이 2 반복 구조로 BFS

        # queue = collections.deque([root])

        # while queue:
        #     node = queue.popleft()
        #     # 부모 노드로부터 하향식 스왑
        #     if node:
        #         node.left, node.right = node.right, node.left

        #         queue.append(node.left)
        #         queue.append(node.right)

        # return root

        # 풀이 3 반복 구조로 DFS

        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root
