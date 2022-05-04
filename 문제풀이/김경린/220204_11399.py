def withdrawTime(times: list):
    sum = 0

    for i in range(len(times)):
        time = 0
        for j in range(i+1):
            time += times[j]
        sum += time

    return sum


case = int(input())
times = list(map(int, input().split()))
times.sort()
print(withdrawTime(times))
