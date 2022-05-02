# 두 정렬 리스트의 병합
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if(not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


list1 = ListNode(4, None)
list2 = ListNode(2, list1)
list3 = ListNode(1, list2)

list4 = ListNode(4, None)
list5 = ListNode(3, list4)
list6 = ListNode(1, list5)

print(mergeTwoLists(list3, list6).next.next.next.val)
