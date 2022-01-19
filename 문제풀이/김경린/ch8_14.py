
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def merge_list(l1: ListNode, l2: ListNode, merge: ListNode):
    if not l1:
        while l2:
            merge.next = l2
            l2 = l2.next
        return merge
    elif not l2:
        while l1:
            merge.next = l1
            l1 = l1.next
        return merge

    if l1.val < l2.val:
        merge.next, l1 = l1, l1.next
        merge_list(l1, l2, merge.next)
    else:
        merge.next, l2 = l2, l2.next
        merge_list(l1, l2, merge.next)


l1_tmp, l2_tmp = map(str, input().split(', '))
l1_tmp = l1_tmp.split('->')
l2_tmp = l2_tmp.split('->')


l1_head = []
l2_head = []

l1 = ListNode(int(l1_tmp[0]))
l1_head = l1
for i in range(len(l1_tmp)-1):
    l1.next = ListNode(int(l1_tmp[i+1]))

    l1 = l1.next

l2 = ListNode(int(l2_tmp[0]))
l2_head = l2
for i in range(len(l2_tmp)-1):
    l2.next = ListNode(int(l2_tmp[i+1]))
    l2 = l2.next

merge_head = ListNode()
merge = merge_list(l1_head, l2_head, merge_head)

merge_head = merge_head.next
while merge_head:
    print(merge_head.val)
    merge_head = merge_head.next
