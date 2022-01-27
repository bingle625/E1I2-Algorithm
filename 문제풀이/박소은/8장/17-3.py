def swapPairs(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        
        # 스왑된 값 리턴받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head