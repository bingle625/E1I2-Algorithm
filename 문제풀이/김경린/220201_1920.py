def numInList(nums, num):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start+end)//2
        if nums[mid] == num:
            return 1
        elif nums[mid] < num:
            start = mid + 1
        else:
            end = mid-1
    return 0


listNum_A = int(input())
listA = list(map(int, input().split()))
listA.sort()
listNum_B = int(input())
listB = list(map(int, input().split()))

for num in listB:
    print(numInList(listA, num))
