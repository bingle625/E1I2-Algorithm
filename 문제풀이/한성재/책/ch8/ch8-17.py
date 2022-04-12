# 17번 페어의 노드 스왑

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


# 값만 교환
list4 = ListNode(4, None)
list3 = ListNode(3, list4)
list2 = ListNode(2, list3)
list1 = ListNode(1, list2)

swapPairs(list1)

# list5 = ListNode(5, list4)
# list6 = ListNode(6, list5)
