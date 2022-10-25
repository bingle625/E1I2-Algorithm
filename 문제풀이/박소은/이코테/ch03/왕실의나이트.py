# 수평 두 칸-수직 한 칸 OR 수직 두 칸-수평 한 칸
# p.115

move = input()
column, row = move[0], move[1]
result = 0

if column != 'a' and column != 'h':
    if '3' <= row <= '6':
        result += 4
    else:
        result += 2
else:
    if '3' <= row <= '6':
        result += 2
    else:
        result += 1

if row != '1' and row != '8':
    if 'c' <= column <= 'f':
        result += 4
    else:
        result += 2
else:
    if 'c' <= column <= 'f':
        result += 2
    else:
        result += 1

print(result)