# A Rank Problem
# n 팀이 m 팀을 이겼다고 가정하자.
# if n < m: no change
# if n > m: m+1, m+2, ... n 팀의 랭킹 1씩 상승, m 팀이 n 팀 자리로.

from typing import List

class ListNode(object):
    def __init__(self, val, next=None, rank=1):
        self.val = val
        self.next = next

def rank(t_num: int, g_list: List) -> ListNode:
    ptr = head = ListNode(0)

    # 초기 연결리스트(T1 ~ Tn)
    for i in range(1, t_num + 1):
        ptr.next = ListNode(i)
        ptr = ptr.next
    
    for str in g_list:
        winner, loser = str.split()
        winner, loser = int(winner[1]), int(loser[1])
        loser_ptr, winner_ptr = head, head.next  # winner_ptr: winner 노드 / loser_ptr: loser 노드의 바로 앞의 노드

        while True:
            if winner_ptr.next.val == winner:   # 순위 높은 팀이 이긴 경우: 순위 변동 X
                break
            winner_ptr = winner_ptr.next
            
            if loser_ptr.next.val == loser:     # 순위 낮은 팀이 이긴 경우
                while winner_ptr.val != winner:    # winner_ptr 마저 찾기
                    winner_ptr = winner_ptr.next

                loser_ptr.next, winner_ptr.next, temp = loser_ptr.next.next, loser_ptr.next, winner_ptr.next
                winner_ptr.next.next = temp
                break
            loser_ptr = loser_ptr.next


    return head.next

t_num, game_num = map(int, input().split())
g_list = []
for _ in range(game_num):
    g_list.append(input())

node = rank(t_num, g_list)
while node is not None:
    print('T' + str(node.val), end=' ')
    node = node.next