# 1065번 한수

def Is_han(num: int) -> bool:
    if num < 100:
        return True
    elif num == 1000:
        return False
    else:
        a = num % 10
        b = num // 10 % 10
        c = num // 100 % 10
        if c - b == b - a:
            return True
        else:
            return False


num = int(input())
hansu = 0
for i in range(1, num+1):
    if(Is_han(i)):
        hansu += 1

print(hansu)
