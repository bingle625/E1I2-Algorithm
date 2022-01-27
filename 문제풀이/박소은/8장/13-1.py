from typing import List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:    # head가 비어있으면 True 반환
            return True
        
        node = head

        # 리스트로 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

listnode1 = ListNode(1, ListNode(2))    # 1->2
listnode2 = ListNode(2, listnode1)      # 2->1->2

sol = Solution()
print(sol.isPalindrome(listnode1))
print(sol.isPalindrome(listnode2))