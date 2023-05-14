# 시간 초과
def solution(number, k):
    answer = []
    
    k = len(number) - k
    start = 0
    fin = len(number) - k + 1
    range_number = number[:fin]
  
    while k > 0:
        max_num = max(range_number)
        answer.append(max_num)
        fin += 1
        start += range_number.index(max_num) + 1
        range_number = number[start : fin]
        k -= 1
    
    
    return ''.join(answer)


# 가장 큰 수를 뽑으려면 전체 길이에서 k-1를 빼고 그 중 가장 큰 수가 첫번째 수
# 1 9 2 4
# 1 9 2  9
# 2 4 
#   range_number = range_number[range_number.index(max_num)+1 : ] + [number[len(number) - k + 1]]


# 정답풀이
# 뺄 숫자만 계산. stack에 숫자를 넣고 다음 수랑 비교하며 작은 숫자 k개 뺌 
def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        while len(answer) and k > 0 and num > answer[-1] :
            answer.pop()
            k -= 1
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)

