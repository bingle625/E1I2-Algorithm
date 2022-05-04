N, M = map(int, input().split())

num_arr = list(map(int, input().split()))

start = max(num_arr)
end = sum(num_arr)

while start <= end:
    mid = (start + end) // 2
    sum1 = 0
    b_ray_length = 1
    for i in range(N):
        if sum1 + num_arr[i] > mid:
            sum1 = num_arr[i]
            b_ray_length += 1
        else:
            sum1 += num_arr[i]

    if b_ray_length > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)