# 15 역순 연결 리스트

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)


list1 = ListNode(4, None)
list2 = ListNode(2, list1)
list3 = ListNode(1, list2)

list4 = ListNode(4, None)
list5 = ListNode(3, list4)
list6 = ListNode(1, list5)
