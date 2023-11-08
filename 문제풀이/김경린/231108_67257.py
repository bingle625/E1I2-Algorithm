from itertools import permutations
from collections import deque
from copy import deepcopy

def calc(operator, expression):
    for op in operator:
        tmp = deque([])
        while len(expression):
            val = expression.popleft()
            if val not in operator:
                tmp.append(val)
            else:
                if val == op:
                    if len(tmp) > 0 and len(expression) > 0:
                        num1 = tmp.pop()
                        num2 = expression.popleft()

                        if op == '+':
                            tmp.append(int(num1)+int(num2))
                        elif op == '-':
                            tmp.append(int(num1)-int(num2))
                        elif op == '*':
                            tmp.append(int(num1)*int(num2))
                else:
                    tmp.append(val)
                    
        expression = deepcopy(tmp)
        
    return tmp[0]

def solution(expression):
    answer = 0
    expression_splited = deque([])
    operator = set([])
    last_idx = 0
    for i in range(len(expression)):
        if expression[i] =='*' or expression[i]=='-' or expression[i]=='+':
            expression_splited.append(''.join(expression[last_idx: i]))
            last_idx = i+1
            operator.add(expression[i])
            expression_splited.append(expression[i])
            
    expression_splited.append(''.join(expression[last_idx:]))
            
    operators = list(permutations(operator, len(operator)))
    
    for op in operators:
        new_val = calc(op, deepcopy(expression_splited))
        answer = max(answer, abs(new_val))
    
    return answer