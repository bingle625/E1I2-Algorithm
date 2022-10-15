

def countBracket(Stack):
    closedBracket = 0  # ')'의 개수
    while not Stack.isEmpty():
        lastItem = Stack.pop()  # 스택에서의 마지막 문자

        if lastItem == ')':
            closedBracket += 1
        elif lastItem == '(':
            closedBracket -= 1
        else:  # 괄호 외의 다른 문자가 입력된 경우
            print('NO')
            return

        if closedBracket < 0:  # 닫힌 괄호의 개수가 음수가 되면 즉시 종료
            print('NO')
            return
    # 모두 돌고나서 괄호 개수가 0이 되었는지 확인

    if closedBracket == 0:
        print('YES')
    else:
        print('NO')

    return


stack = Stack()  # stack이름의 스택 생성

N = int(input())
for _ in range(N):
    stk = Stack()
    inputList = list(input())
    for i in range(len(inputList)):  # 스택의 특성상 push로 입력받아봅시다...
        stk.push(inputList[i])
    countBracket(stk)
