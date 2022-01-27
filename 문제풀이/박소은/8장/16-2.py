
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            print(l1.val, l2.val)
            sum = 0

            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            print(carry, val)
            head.next = ListNode(val)
            head = head.next
            print("val: ", head.val)
        
        return root.next

# l1
l1 = ListNode(2)
listnode1 = ListNode(4)
listnode2 = ListNode(3)
l1.next = listnode1
listnode1.next = listnode2


# l2
l2 = ListNode(5)
listnode3 = ListNode(6)
listnode4 = ListNode(4)
l2.next = listnode3
listnode3.next = listnode4

sol = Solution()
print(sol.addTwoNumbers(l1, l2).val)