class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head

    # 런너를 이욯해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next    # 빠른 런너는 2칸씩 이동
        rev, rev.next, slow = slow, rev, slow.next
    if fast:    # 입력값이 홀수일 때 slow를 한 칸 더 이동
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev