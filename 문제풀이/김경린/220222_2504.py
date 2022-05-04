
from collections import deque



def is_wellformed(strs):
    if len(strs)%2==1:
        return False
    cleaned=[]
    while strs:
        tmp = strs.pop()
        if tmp==')' or tmp==']':
            cleaned.append(tmp)
        elif tmp=='(':
            if len(cleaned)>0:
                if cleaned[-1]==')':
                    cleaned.pop()
            else:
                cleaned.append(tmp)
        elif tmp=='[':
            if len(cleaned)>0:
                if cleaned[-1]==']':
                    cleaned.pop()
            else:
                cleaned.append(tmp)
    if len(cleaned)==0:
        return True
    else:
        return False

def cal_strs(strs):
    cleaned=[]
    while strs:
        tmp = strs.popleft()
        if tmp=='(' or tmp=='[':
            cleaned.append(tmp)
        elif tmp==')':
            if cleaned[-1]=='(':
                cleaned.pop()
                cleaned.append(2)
            elif len(cleaned)>1:
                sum = 0
                while type(cleaned[-1])==int:
                    sum += cleaned.pop()
                if cleaned[-1]=='(':
                    cleaned.pop()
                    sum *=2
                cleaned.append(sum)
            else:
                cleaned.append(')')
        elif tmp==']':
            if cleaned[-1]=='[':
                cleaned.pop()
                cleaned.append(3)
            elif len(cleaned)>1:
                sum = 0
                while type(cleaned[-1])==int:
                    sum += cleaned.pop()
                if cleaned[-1]=='[':
                    cleaned.pop()
                    sum *=3
                cleaned.append(sum)
            else:
                cleaned.append(']')
        
    #남은 수 합 계산
    result = 0
    for num in cleaned:
        result += num

    return result

strs = list(input())

if not is_wellformed(strs[:]):
    print(0)
else:
    strs = deque(strs)
    print(cal_strs(strs))

        
    


