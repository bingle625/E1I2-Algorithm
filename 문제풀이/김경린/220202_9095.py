case = int(input())

for x in range(case):
    n = int(input())

    sum_num = [0 for _ in range(n+1)]
    sum_num[1] = 1

    for i in range(2, n+1):
        for j in range(1, 4 if i > 3 else i):
            if i-j <= 3:
                sum_num[i] += sum_num[i-j]
            else:
                sum_num[i] += sum_num[i-j]
        if i < 4:
            sum_num[i] += 1

    print(sum_num[n])
