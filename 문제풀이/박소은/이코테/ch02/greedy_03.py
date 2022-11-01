# p.313 03. 문자열 뒤집기
# 0과 1로만 이루어진 문자열 S

# AB -> 1번
# ABA -> 1번
# ABAB -> 2번

s = input()

current = s[0]
field = 1
for char in s:
    if current != char:
        current = char
        field += 1

print(field // 2)