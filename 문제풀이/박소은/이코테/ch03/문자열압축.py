def solution(s):
    answer = 1000
    
    for unitNum in range(1, len(s)//2 + 1):
        currentChar = s[0:unitNum]  # 현재 겹치는 문자열
        currentIndex = unitNum  # 문자열 자를 때 시작하는 index
        currentLength = len(s)
        isSame = False
        
        # unitNum씩 끊어서 같은지 확인하고, 같으면 총 length에서 -unitNum 하면 됨.
        while True:
            if currentIndex+unitNum > len(s):  # 더 이상 끊지 못하면 break
                break
                
            if currentChar == s[currentIndex : currentIndex+unitNum]:
                # 같은 문자열 반복인 경우
                isSame = True
                currentLength -= unitNum
            else:
                # 다른 문자열이 나왔을 경우
                if isSame:  # 이때까지 겹친 문자열이 2개 이상인 경우 겹치는 숫자도 넣어주어야함.
                    currentLength += 1
                currentIndex += unitNum # 다음 문자열 index로 넘어가기
                currentChar = s[currentIndex : currentIndex+unitNum]    # 자른 문자열 저장
                isSame = False

            currentIndex += unitNum # 다음 문자열 자르기
        
        if currentLength < answer:
            answer = currentLength
    return answer

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
