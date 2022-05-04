# 풀이 2: 삽입 정렬의 비교 조건 개선

def insertionSortList(self, head: ListNode) -> ListNode:
    # 초깃값 변경
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
            cur = parent
        
    return parent.next