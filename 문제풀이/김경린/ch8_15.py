
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reverse(l1: ListNode):
    l_tmp, l1.next, l1 = l1, None, l1.next
    while l1:
        r_tmp, l1.next = l1.next, l_tmp
        l_tmp, l1 = l1, r_tmp

    return l_tmp


l1_tmp = input()
l1_tmp = l1_tmp.split('->')


l1 = ListNode(int(l1_tmp[0]))
l1_head = l1
for i in range(len(l1_tmp)-1):
    l1.next = ListNode(int(l1_tmp[i+1]))
    l1 = l1.next

reverse_list = reverse(l1_head)

while reverse_list:
    print(reverse_list.val)
    reverse_list = reverse_list.next
