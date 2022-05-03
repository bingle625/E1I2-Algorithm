# 팰린드롬 연결리스트

import re
from typing import List
from asyncio.windows_events import NULL
import collections


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # 내 풀이 1648ms
# def isPalindrome(head: ListNode) -> bool:
#     new_deque = collections.deque()
#     while head != None:
#         new_deque.append(head.val)
#         head = head.next

#     while len(new_deque) > 1:
#         if new_deque.popleft() == new_deque.pop():
#             continue
#         else:
#             return False
#     return True

# # 리스트

# def isPalindrome(head: ListNode) -> bool:
#     q: list = []

#     if not head:
#         return True

#     node = head

#     while node is not None:
#         q.append(node.val)
#         node = node.next

#     while len(q) > 1:
#         if q.pop(0) != q.pop():
#             return False

#     return True


# 런너 풀이법

def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # 이 부분을 잘 모르겠음
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


listnode1 = ListNode(1, ListNode(2))    # 1->2
listnode2 = ListNode(2, listnode1)      # 2->1->2


print(isPalindrome(listnode1))
print(isPalindrome(listnode2))
