import math
# 틀린 풀이
# 반례 3*5
# def solution(w,h):
#     a = math.ceil(w / h) * h if w > h else math.ceil(h / w) * w
#     answer = w * h - a
#     return answer

# 시간 초과 + 오답
# def solution(w,h):
#     if w > h:
#         a = w / h
#         num = h
#     else:
#         a = h / w
#         num = w
        
#     rect = 0
#     for i in range(1, num + 1):
#         rect += math.ceil(a*i) - math.floor(a*(i-1))
#     return w*h-rect

def solution(w,h):
    a = math.gcd(w,h)
    answer = w * h - (w+h-a)
    return answer