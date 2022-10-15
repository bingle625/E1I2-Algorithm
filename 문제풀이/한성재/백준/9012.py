N, M = map(int, input().rstrip().split())

arr = list([10005]*M)

for i in range(N):
    temp = list(map(int, input().rstrip().split()))
    for k in range(len(temp)):
        if temp[k] < arr[k]:
            print(temp[k], arr[k])
            arr[k] = temp[k]

print(max(arr))
