from sys import stdin

def isEnoughMoney(num):
    sum = 0
    for i in range(len(costs)):
        if costs[i]<=size - sum:
            sum +=  costs[i]
        else:
            num -= 1
            if num<0:
                return False
            sum = 0
            if costs[i]<=size - sum:
                sum += costs[i]
            else:
                return False
    return True

day, num = map(int,stdin.readline().split())
costs = []

for i in range(day):
    cost = int(stdin.readline())
    costs.append(cost)


l = max(costs)
r = sum(costs)

while l<r:
    mid = l + (r-l)//2
    size = mid
    ok = isEnoughMoney(num-1)
    if ok:
        r = mid
    else:
        l = mid + 1


print(r)