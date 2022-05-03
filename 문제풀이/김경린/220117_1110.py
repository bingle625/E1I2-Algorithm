def calculate(num):
    cnt = 0
    tmp = num
    while True:
        cnt += 1
        tmp_2 = tmp//10 + tmp % 10
        tmp = tmp % 10*10 + tmp_2 % 10
        if tmp == num:
            return cnt


num = int(input())
print(calculate(num))
