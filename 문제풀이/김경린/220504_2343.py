# 1 2 3 4 5  6 7  8  9
# 45 / 3 
# 15 45
# 넘을 것 같으면 바로 끝

def isInBlueray(leftBlueray):
    sum = 0
    for i in range(len(lectures)):
        if lectures[i]<=size - sum:
            sum +=  lectures[i]
        else:
            leftBlueray -= 1
            if leftBlueray<0:
                return False
            sum = 0
            if lectures[i]<=size - sum:
                sum += lectures[i]
            else:
                return False
    return True

lectureNum, bluerayNum = map(int,input().split())

lectures = list(map(int,input().split()))

l = sum(lectures)//bluerayNum
r = sum(lectures)

while l<r:
    mid = l + (r-l)//2
    size = mid
    leftBlueray = bluerayNum - 1
    ok = isInBlueray(leftBlueray)
    if ok:
        r = mid
    else:
        l = mid + 1


print(r)