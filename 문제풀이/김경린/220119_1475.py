from functools import cmp_to_key


def set_num(num: str):
    num = num.replace('9', '6')
    max = num.count('6')

    if max % 2 == 0:
        max = max // 2
    else:
        max = max//2+1

    change = 0
    for x in range(10):
        if x == 6:
            continue
        if num.count(str(x)) > max:
            max = num.count(str(x))

    cnt = max

    return cnt


num = input()
print(set_num(num))
