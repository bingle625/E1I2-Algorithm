
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val)
        head = head.next


def remove(r, people: ListNode):
    head = people
    while people:
        if r > 2 and people.next:
            for i in range(r-2):
                people = people.next
                if not people:
                    return head
        if people.next:
            people.next = people.next.next
            people = people.next
        else:
            return head
    return head


num = int(input())
l1 = ListNode(1)
head = l1
for i in range(num-1):
    l1.next = ListNode(i+2)
    l1 = l1.next

round = int(input())
for i in range(round):
    remove_num = int(input())
    head = remove(remove_num, head)

print_list(head)
