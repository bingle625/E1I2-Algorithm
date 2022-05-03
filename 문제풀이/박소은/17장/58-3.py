# 풀이 3: 내장 함수를 이용하는 실용적인 방법

def sortList(self, head: ListNode) -> ListNode:
    # 연결 리스트 -> 파이썬 리스트
    p = head
    lst: List = []
    while p:
        lst.append(p.val)
        p = p.next
    
    # 정렬
    lst.sort()

    # 파이썬 리스트 -> 연결 리스트
    p = head
    for i in range(len(lst)):
        p.val = list[i]
        p = p.next
    return head