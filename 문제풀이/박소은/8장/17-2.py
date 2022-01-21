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
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next

            root.print_all_val()
            prev.print_all_val()
        
        return root.next

l1 = ListNode(1)
listnode1 = ListNode(2)
listnode2 = ListNode(3)
listnode3 = ListNode(4)
l1.next = listnode1
listnode1.next = listnode2
listnode2.next = listnode3

sol = Solution()
print(sol.swapPairs(l1).val)
