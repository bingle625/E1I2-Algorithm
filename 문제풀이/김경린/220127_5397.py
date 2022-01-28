
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DList:

    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def insert(self, value, node):
        if self.is_empty():
            self.head = ListNode(value)
            self.tail = ListNode(None, self.head)
            self.head.next = self.tail
        else:
            if node.next:
                tmp = node.next
                new_node = ListNode(value, node, tmp)
                node.next = new_node
                tmp.prev = new_node
            else:
                new_node = ListNode(value, node, None)
                node.next = new_node


def print_list(head):
    while head:
        if head.val == None:
            break
        print(head.val, end="")
        head = head.next
    print("")


cnt = int(input())

for i in range(cnt):
    ans = DList()
    strs = input()
    for x in strs:
        if x == '<':
            if ans.is_empty():
                continue
            else:
                if cur == None:
                    continue
                elif cur == ans.head:
                    cur.prev = None
                cur = cur.prev

        elif x == '>':
            if ans.is_empty():
                continue
            else:
                if cur.next.val != None:
                    cur = cur.next
        elif x == '-':
            if ans.is_empty() or cur.val == None:
                continue
            elif cur == ans.head:
                cur.next = None
                ans.head = None
            else:
                tmp = cur.next
                cur = cur.prev
                if cur != None:
                    cur.next = tmp
                else:
                    ans.head = tmp
            ans.size -= 1
        else:
            if ans.is_empty():
                ans.insert(x, None)
                cur = ans.head
            else:
                if cur == None:
                    new_node = ListNode(x, None, ans.head)
                    ans.head.prev = new_node
                    ans.head, cur = new_node, new_node

                else:
                    ans.insert(x, cur)
                cur = cur.next
            ans.size += 1

    print_list(ans.head)
