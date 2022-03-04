# 10799번: 쇠막대기

def cut(s: str) -> int:
    sum = 0
    (1(111(11))) 요런식으로!!
    lazer = []
    lazer.append(0)
    lazer_bool = False
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(1)
            lazer_bool = True
            if lazer[-1] != 0:
                

        else:
            stack.pop()

            if lazer_bool == True:  # lazer인 경우
                lazer_bool = False
                if stack:
                    lazer[-1] += 1
                continue
            
            if len(stack) < len(lazer):
                i = len(lazer) - len(stack)
                for elem in range(i, len(lazer)):
                    sum += elem
                sum += 1
            else:
                sum += lazer[-1] + 1
            lazer_bool = False

            if not stack:   # stack에 남은 요소가 없다면
                lazer.pop()
            else:
                lazer.append(0)
            
    return sum

print(cut("()(((()())(())()))(())"))