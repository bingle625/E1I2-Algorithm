# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    longest: int = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node: TreeNode) -> int:
            # 예외 처리
            if not node:
                return -1

            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 루트 노드인 이진트리에서 가장 긴 경로
            self.longest = max(self.longest, left+right+2)

            # 상태값(현재 노드를 루트 노드로 하는 트리의 리프노드에서 현재 노드 까지으 거리)
            return max(left, right)+1
