from collections import deque

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        a.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True
