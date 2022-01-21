def swapPairs(self, head: ListNode) -> ListNode:
    cur head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
        
        return head