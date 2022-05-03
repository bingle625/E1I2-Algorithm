def cnt_num(num):
    cnt = 0
    for i in range(1, num+1):
        digit = str(i)
        is_sequence = True
        if len(digit) > 1:
            d = int(digit[1]) - int(digit[0])
            for j in range(1, len(digit)):
                if int(digit[j]) - int(digit[j-1]) != d:
                    is_sequence = False
                    break
            if is_sequence:

                cnt += 1
        else:
            cnt += 1
    return cnt


num = int(input())
print(cnt_num(num))
