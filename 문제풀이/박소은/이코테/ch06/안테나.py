
N = int(input())
array = list(map(int, input().split()))
array.sort()

if N%2 == 1:
    print(array[N])
else:
    average = avg(array)
    if abs(average - 