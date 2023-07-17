# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_node(self):
        temp = self
        while temp:
            print(temp.val, end="-")
            temp = temp.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        else:
            result = ptr = ListNode()

        while list1 and list2:
            if list1.val >= list2.val:
                ptr.next = list2
                ptr = ptr.next
                list2 = list2.next
            else:
                ptr.next = list1
                ptr = ptr.next
                list1 = list1.next
        
        if list1 or list2:
            ptr.next = list1 if list1 else list2
        
        return result.next


# Debugging
list1 = ListNode(2, ListNode(4, ListNode(6, None)))
list2 = ListNode(1, ListNode(3, ListNode(5, None)))
sol = Solution()
result_nodes = sol.mergeTwoLists(list1, list2)
result_nodes.print_node()