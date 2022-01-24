
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val)
        head = head.next
