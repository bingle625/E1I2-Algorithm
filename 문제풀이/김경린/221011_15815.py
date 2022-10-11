from sys import stdin
# from collections import deque

def isNum(x):
    if x == '+' or x == '-' or x == '*' or x == '/':
        return False
    return True
calc = list(input())
temp = []
while len(calc) > 1:
    x = calc.pop()
    if x == '+':
        num1 = calc.pop()
        num2 = calc.pop()
        if isNum(num1) and isNum(num2):
            calc.append(int(num1)+int(num2))
            while len(temp):
                calc.append(temp.pop())
        else:
            calc.append(num2)
            calc.append(num1)
            temp.append(x)
        
    elif x == '-':
        num1 = calc.pop()
        num2 = calc.pop()
        if isNum(num1) and isNum(num2):
            calc.append(int(num2)-int(num1))
            while len(temp):
                calc.append(temp.pop())
        else:
            calc.append(num2)
            calc.append(num1)
            temp.append(x)

    elif x == '*':
        num1 = calc.pop()
        num2 = calc.pop()
        if isNum(num1) and isNum(num2):
            calc.append(int(num1)*int(num2))
            while len(temp):
                calc.append(temp.pop())
        else:
            calc.append(num2)
            calc.append(num1)
            temp.append(x)
 
    elif x == '/':
        num1 = calc.pop()
        num2 = calc.pop()
        if isNum(num1) and isNum(num2):
            calc.append(int(num2)//int(num1))
            while len(temp):
                calc.append(temp.pop())
        else:
            calc.append(num2)
            calc.append(num1)
            temp.append(x)
    else:
        temp.append(x)

        
print(calc[0])
            

