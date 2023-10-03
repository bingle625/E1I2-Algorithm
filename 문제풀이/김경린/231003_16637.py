from collections import deque
import sys


n = int(input())
command = list(input())


#  기존 풀이 -> 괄호가 생길 수 있는 곳을 brackets에 저장 후 모두 계산

# nums = len(command)//2

# def calc(brackets):
#     # cmds = deque(cmds)
#     result = deque()
#     result.append(int(command[0]))
#     for i in range(nums):
#         num1 = result.pop()
#         if brackets[i]:
#             op = command[2*i+1]
#             if op == '+':
#                 result.append(num1 + int(command[2*i+2]))
#             elif op == '-':
#                 result.append(num1 - int(command[2*i+2]))
#             elif op == '*':
#                 result.append(num1 * int(command[2*i+2]))
#         else:
#             result.append(num1)
#             result.append(command[2*i+1])
#             result.append(int(command[2*i+2]))
#     # print("bf",result)
#     while len(result) > 2:
#         num1 = result.popleft()
#         op = result.popleft()
#         num2 = result.popleft()

#         if op == '+':
#             result.appendleft(num1+num2)
#         elif op == '-':
#             result.appendleft(num1-num2)
#         elif op == '*':
#             result.appendleft(num1*num2)
#     # print("af",result)
#     return result[-1]

max_value = -sys.maxsize

# def dfs(brackets, idx):
#     global max_value
#     if idx >= len(brackets):
#         value = calc(brackets)
#         max_value = max(max_value, value)
#         return 
#     else:
#         if brackets[idx-1] == True:
#             brackets[idx] = False
#             dfs(brackets, idx+1)
#         else:
#             dfs(brackets, idx+1)
#             brackets[idx] = True
#             dfs(brackets, idx+1)
#             brackets[idx] = False
    

# dfs([0 for _ in range(nums)], 0)
# print(max_value)


# 괄호가 생길 수 있는 규칙으로 접근

def calc(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2

def dfs(i, value):
    global max_value

    if i == n:
        max_value = max(max_value, value)
        return
    else:
        #괄호 o
        if i + 4 <= n:
            dfs(i+4, calc(value, command[i], calc(int(command[i+1]),command[i+2], int(command[i+3]))))
        #괄호 x
        if i + 2 <= n:
            dfs(i+2, calc(value, command[i], int(command[i+1])))

dfs(1, int(command[0]))
print(max_value)