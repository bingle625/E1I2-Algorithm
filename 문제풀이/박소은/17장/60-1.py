# 풀이 1: 삽입 정렬

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortLst(head: ListNode) -> ListNode:
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next
        cur = parent

        print_all(parent.next)
        print()
        print_all(head)
        print("-----------------------")
    return cur.next

def print_all(head: ListNode) -> None:
    while head:
        print(head.val)
        head = head.next

a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d
insertionSortLst(a)