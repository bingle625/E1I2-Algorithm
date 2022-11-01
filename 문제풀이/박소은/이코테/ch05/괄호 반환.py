# p.346 18. 괄호 반환(https://school.programmers.co.kr/learn/courses/30/lessons/60058)

from collections import deque

def solution(p):
    answer = ''
    s = p
    if not s:   # 빈 문자열인 경우 -> 빈 문자열 반환
        return ''
    index = balancedStr(s)
    u, v = p[0:index+1], p[index+1:]    # 문자열 w를 두 균형잡힌 문자열 u, v로 나누기
    
    if isCorrect(u):
        answer = u + solution(v)
        return answer
    else:
        answer = '(' + solution(v) + ')'
        temp = list(u[1:len(u)-1])    # u의 첫 번째와 마지막 문제 제거
        for idx in range(len(temp)):
            if temp[idx] == '(':
                temp[idx] = ')'
            else:
                temp[idx] = '('
        return answer + ''.join(temp)

def balancedStr(s): # 균형잡힌 괄호 문자열 u의 마지막 index 반환
    left = 0
    right = 0
    
    for idx in range(len(s)):
        if s[idx] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return idx
    return 0

def isCorrect(s):
    queue = deque([])
    for idx in range(len(s)):
        if s[idx] == '(':
            queue.append('(')
        else:
            if not queue:   # queue가 비었는데 pop을 하는 경우
                return False
            else:
                queue.pop()
            
    if not queue:
        return True
    else:
        return False
