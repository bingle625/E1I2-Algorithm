#2805 나무자르기

N,M = map(int,input().split())

trees = list(map(int,input().split()))

trees.sort(reverse=True)

def getTree():
    start,end= 1, trees[0]

    while start <= end:
        mid = (start + end) // 2
        sum1 = 0
        for i in range(N):
            if trees[i] >= mid:
                sum1 += (trees[i] - mid)
        
        if sum1 >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end
        
print(getTree())