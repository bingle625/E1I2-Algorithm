def solution(s):
    answer = 0
    
    mini = len(s)
    temp =""
    for i in range(1,len(s)):
        length = len(s)
        cnt = 1
        temp = s[:i]
        pointer = 0
        while pointer + 2*i < len(s)+1:
            if temp == s[pointer + i : pointer+ 2*i]:
                pointer += i
                length -= i
                cnt += 1
            else:
                if cnt == 1:
                    pointer += i
                else:
                    pointer += i
                    length += len(str(cnt))
                    print(cnt)
                    cnt = 1
                temp = s[pointer : pointer + i]
        
        if cnt > 1:
            length += len(str(cnt))
        
        mini = min(mini,length)
    answer = mini
    
    return answer

print(solution("xxxxxxxxxxyyy"))
