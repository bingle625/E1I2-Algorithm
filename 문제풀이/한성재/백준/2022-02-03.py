# 10799번 쇠막대기

def laser_it(still_set: list) -> int:
    sum = 0

    stack = []
    IsLaser = False

    for still in still_set:
        if still == '(':
            stack.append(still)
            IsLaser = True
        else:
            if(IsLaser):
                # 레이저이면 스택에 쌓인 숫자 *1
                stack.pop()
                sum += len(stack)
                IsLaser = False
            else:
                # 레이저가 아니라면 그냥 +1
                stack.pop()
                sum += 1

    return sum


still = list(map(str, input()))


print(laser_it(still))
