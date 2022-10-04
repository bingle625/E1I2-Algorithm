numbers = list(map(int, input()))
res = numbers[0]
for number in numbers[1:]:
    if (number <= 1) or (res <= 1):
        res += number 
    else:
        res *= number

print(res)