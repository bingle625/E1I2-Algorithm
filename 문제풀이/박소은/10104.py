# 풀이 1: 연결 리스트
from typing import List

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def party_invitation(friend_num: int, round_num: int, removal_num: List) -> ListNode:
    friends_list = head = ListNode(0)

    # 1 ~ friend_num으로 구성된 friend_list 만들기
    for j in range(1, friend_num + 1):
        friends_list.next = ListNode(j)
        friends_list = friends_list.next
    
    for i in range(0, round_num):
        friends_list = head.next
        prev = head
        j = 1

        # 친구 삭제하기
        while friends_list is not None:
            if j % removal_num[i] == 0:
                prev.next = prev.next.next
            else:
                prev = prev.next
            friends_list = friends_list.next
            j += 1
    
    return head.next

f_num = int(input())
round_num = int(input())
removal_num = []
for _ in range(0, round_num):
    removal_num.append(int(input()))

f_list = party_invitation(f_num, round_num, removal_num)
while f_list is not None:
    print(f_list.val)
    f_list = f_list.next




# 풀이 2: 파이썬 리스트
# 런타임 에러

# def party_invitation(f_num: int, round: int, r_num: List) -> List:
#     f_list = [n for n in range(1, f_num + 1)]
#     removal_num = 0
#     r_list = []

#     for i in range(0, round):
#         for j in range(1, f_num + 1):
#             if j % r_num[i] == 0:
#                 r_list.append(j)
#                 removal_num += 1
#         f_num -= removal_num

#         k = 0
#         while removal_num > 0:
#             if f_list[k] in r_list:
#                 del f_list[k]
#                 removal_num -= 1
#             k += 1

#         r_list = []
    
#     return f_list

# # input 입력
# f_num = int(input())
# round_num = int(input())
# removal_num = []
# for _ in range(0, round_num):
#     removal_num.append(int(input()))

# f_list = party_invitation(f_num, round_num, removal_num)
# for i in f_list:
#     print(i)