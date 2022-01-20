# 유효한 팰린드롬

is_palindrome = 1

tmp = input()
str = tmp.replace(" ", "")
for idx in range(len(str)):
    if idx >= len(str)/2:
        break
    if str[idx] != str[len(str)-idx-1]:
        is_palindrome = 0

if is_palindrome == 0:
    print('False')
else:
    print(True)
