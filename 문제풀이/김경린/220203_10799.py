
sum = 0
cnt = 0
stack = list(input())
while len(stack):
    tmp = stack.pop()
    if tmp == ')':
        tmp2 = stack.pop()
        if tmp2 == '(':
            sum += cnt

        else:
            stack.append(tmp2)
            cnt += 1
    else:
        sum += 1
        cnt -= 1
print(sum)
