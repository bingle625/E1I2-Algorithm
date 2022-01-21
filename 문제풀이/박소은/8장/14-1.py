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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            print("swap: ", end="")
            if l1 and l2:
                print(l1.val, l2.val)
            l1, l2 = l2, l1
        if l1:
            print("재귀: ", end="")
            if l1 and l2:
                print(l1.val, l2.val)
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


# l1
l1 = ListNode(1)
listnode1 = ListNode(2)
listnode2 = ListNode(3)
l1.next = listnode1
listnode1.next = listnode2


# l2
l2 = ListNode(1)
listnode3 = ListNode(3)
listnode4 = ListNode(4)
l2.next = listnode3
listnode3.next = listnode4

sol = Solution()
sol.mergeTwoLists(l1, l2)