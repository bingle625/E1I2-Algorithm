from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_all_val(self):
        temp = self
        while temp.next != None:
            print(temp.val, end=" ")
            temp = temp.next
        print(temp.val)



class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 예외 처리
        if not head or m==n:
            return head
        
        root = start = ListNode(None)
        root.next = head

        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            start.print_all_val()
        start.print_all_val()
        return root.next


l1 = ListNode(1)
listnode1 = ListNode(2)
listnode2 = ListNode(3)
listnode3 = ListNode(4)
listnode4 = ListNode(5)
l1.next = listnode1
listnode1.next = listnode2
listnode2.next = listnode3
listnode3.next = listnode4

sol = Solution()
sol.reverseBetween(l1, 2, 4)