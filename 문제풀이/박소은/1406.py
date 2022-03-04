from typing import List

class ListNode(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def cursor(line: str, inst_list: List) -> List:

    # line으로 ListNode 만들기

    for elem in str:
        ptr.next = ListNode(elem)
        
        ptr = ptr.next
    # 현재 ptr의 위치: 문장의 맨 뒤 문자
    # prev: ptr 바로 전 문자

    for elem in inst_list:
        if elem == 'L':
            pass
        elif elem == 'D':
            pass
        elif elem == 'B':
            pass
        else:   # P $ 일 때
            ptr, ptr.next = ListNode(elem[2]), ptr


inst_list = []
line = input()
num = int(input())
for _ in range(num):
    inst_list.append(input())
print(cursor(line, inst_list))