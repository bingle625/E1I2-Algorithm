# Definition for a binary tree node.
import collections
from turtle import left


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # queue, 즉, 부모 노드 큐 길이만큼 반복하므로,
            # 그 뒤에 들어간 자식노드는 다음 주기에서 반복
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root, left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth
