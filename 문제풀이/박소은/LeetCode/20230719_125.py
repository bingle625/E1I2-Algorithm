# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_str = ""
        for c in s:
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                parsed_str += c

        parsed_str = parsed_str.lower()
        half_len = int(len(parsed_str)/2)

        if len(parsed_str)%2 == 0:
            half=reversed(parsed_str[half_len:])
        else:
            half=reversed(parsed_str[half_len+1:])

        result = True if parsed_str[:half_len] == ''.join(half) else False

        return result


# Solution 2
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        parsed_str = ''.join(c for c in s if c.isalnum())
        l = parsed_str.lower()
        return l == l[::-1]


# Solution 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True