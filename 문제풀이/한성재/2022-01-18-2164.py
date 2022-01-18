# 2164번 카드2
from hashlib import new


def remove_odd(arr: list) -> list:
    new_arr = []
    for i in range(1, len(arr)+1):
        if i % 2 == 0:
            new_arr.append(arr[i-1])
        else:
            continue

    return new_arr


num = int(input())

arr = list(range(1, num+1))

while len(arr) > 1:
    arr = remove_odd(arr)

print(arr[0])
