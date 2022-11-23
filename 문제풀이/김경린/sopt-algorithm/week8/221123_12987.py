from collections import deque
def solution(A, B):
    cnt = 0
    A.sort()
    B.sort()
    B = deque(B)
    for a in A:
        if len(B):
            while len(B) and a >= B[0]:
                B.popleft()
            if len(B):
                B.popleft()
                cnt += 1
        else:
            break
                
    return cnt