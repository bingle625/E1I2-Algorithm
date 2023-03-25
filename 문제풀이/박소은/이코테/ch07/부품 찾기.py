# 부품 N개, 구매 M개

N = int(input())
array = list(map(int, input().split()))
M = int(input())
findList = list(map(int, input().split()))

array.sort()
findList.sort()

for elem in findList:
    if elem in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")