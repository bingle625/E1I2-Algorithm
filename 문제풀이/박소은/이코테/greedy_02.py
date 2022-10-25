# p.312 02. 곱하기 혹은 더하기
# 각 자리가 숫자(0~9)로만 이루어진 문자열 S
# 왼쪽부터 오른쪽으로 이동하며 숫자 사이에 * 혹은 + 넣어 만들 수 있는 가장 큰 수

s = input()
answer = 0

for char in s:
    if char == '0' or char == '1' or answer <= 0:
        answer += int(char)
    else:
        answer *= int(char)

print(answer)