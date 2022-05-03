# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        half, slow, fast = None, head, head
        



testList =  ListNode(4)
testList.next = ListNode(2)
testList.next.next = ListNode(1)
testList.next.next.next = ListNode(3)