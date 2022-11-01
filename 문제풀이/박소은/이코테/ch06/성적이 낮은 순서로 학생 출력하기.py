N = int(input())

array = []
for _ in range(N):
    array.append(tuple(input().split()))

array.sort(key=lambda x : x[1])
print(array)