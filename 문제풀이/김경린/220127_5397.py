

# class ListNode:
#     def __init__(self, val=0, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next


# class DList:

#     def __init__(self):
#         self.head = ListNode(None)
#         self.tail = ListNode(None, self.head)
#         self.head.next = self.tail
#         self.size = 0

#     def is_empty(self):
#         if self.size != 0:
#             return False
#         else:
#             return True

#     def insert(self, value, node):
#         if self.is_empty():
#             self.head = ListNode(value)
#         else:
#             if node.next:
#                 tmp = node.next
#                 new_node = ListNode(value, node, tmp)
#                 node.next = new_node
#                 tmp.prev = new_node
#             else:
#                 new_node = ListNode(value, node, None)
#                 node.next = new_node


# def print_list(head):
#     while head:
#         if head.val == None:
#             break
#         print(head.val, end="")
#         head = head.next
#     print("")


# cnt = int(input())
# cur = None
# for i in range(cnt):
#     ans = DList()
#     strs = input()
#     for x in strs:
#         if x == '<':
#             if ans.is_empty():
#                 continue
#             else:
#                 if cur == None:
#                     continue
#                 elif cur == ans.head:
#                     cur.prev = None
#                 cur = cur.prev

#         elif x == '>':
#             if ans.is_empty():
#                 continue
#             else:
#                 if cur == None:
#                     cur = ans.head
#                 elif cur.next != None:
#                     cur = cur.next
#         elif x == '-':
#             if ans.is_empty() or cur == None or cur.val == None:
#                 continue
#             elif cur == ans.head:
#                 ans.head = cur.next
#                 if ans.head != None:
#                     ans.head.prev = None
#                 cur = None
#             else:
#                 tmp = cur.next
#                 cur = cur.prev
#                 if cur != None:
#                     cur.next = tmp
#                 else:
#                     ans.head = tmp
#             ans.size -= 1
#         else:
#             if ans.is_empty():
#                 ans.insert(x, None)
#                 cur = ans.head
#             else:
#                 if cur == None:
#                     new_node = ListNode(x, None, ans.head)
#                     ans.head.prev = new_node
#                     ans.head, cur = new_node, new_node

#                 else:
#                     ans.insert(x, cur)
#                 cur = cur.next
#             ans.size += 1

#     print_list(ans.head)

from collections import deque


case = int(input())
for i in range(case):
    strs = input()
    strs = deque(list(strs))
    strs_1 = []
    strs_2 = deque()

    while strs:  
        str = strs.popleft()
        if str=='<':
            if len(strs_1)>0:
                str_tmp = strs_1.pop()
                strs_2.appendleft(str_tmp)
        elif str=='>':
            if len(strs_2)>0:
                str_tmp = strs_2.popleft()
                strs_1.append(str_tmp)
        elif str=='-':
            if len(strs_1)>0:
                strs_1.pop()
        else:
            strs_1.append(str)

    strs_1 = ''.join(strs_1)
    strs_2 = ''.join(strs_2)
    
    password = strs_1 + strs_2
    print(password)
