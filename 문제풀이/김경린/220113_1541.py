
def min_sum(cal):
    sum = 0
    new_cal = cal.split('-')

    result = 0

    for i in range(len(new_cal)):
        sum = 0
        if '+' in new_cal[i]:
            nums = new_cal[i].split('+')
            for num in nums:
                sum += int(num)
        else:
            sum += int(new_cal[i])
        if i == 0:
            result += sum
        else:
            result -= sum
    print(result)


cal = input()
min_sum(cal)

a = [0, 1, 2]
del a[1]
print(a[1])
