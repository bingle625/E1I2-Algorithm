
array = []

N = int(input())
for _ in range(N):
    array.append(tuple(input().split()))

array.sort(key= lambda x: (-int(x[1]), x[2], -int(x[3])))

for i in range(N):
    print(array[i][0])