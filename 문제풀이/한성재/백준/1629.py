import collections


a, b, c = map(int, input().split())

numbers = collections.defaultdict(int)

numbers[1] = a


def getRem(a, numb):
    if numb in numbers:
        return numbers[numb]

    if numb % 2 == 0:
        temp = getRem(a, numb//2)
        numbers[numb] = temp*temp
    else:
        temp = getRem(a, numb//2)
        numbers[numb] = temp*temp*a

    return numbers[numb]


print(getRem(a, b) % c)
