# Solution 1: 내 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
                continue
            elif not stack:     # stack이 비었는데 닫는 괄호인 경우
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:   # stack에 일치하는 짝이 없는 경우
                return False
        
        if stack:
            return False
        else:   # stack에 문자가 남은 경우
            return True


# Solution 2: 정돈된 코드(풀이 참고)
from collections import defaultdict

class Solution2:
    def isValid(self, s: str) -> bool:
        paren_dict = defaultdict(str)
        paren_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            if char in paren_dict: # 닫는 괄호일 때
                if not stack or stack.pop() != paren_dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack