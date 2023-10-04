### ord 문자에 맞는 아스키 코드 반환 chr 숫자에 맞는 아스키 코드
## 슬라이딩 윈도우

from collections import defaultdict

w_len, g_len = map(int, input().split(' '))
w = list(input())
s = list(input())

w_list = [0 for _ in range(58)]
sa_list = [0 for _ in range(58)]

for i in range(w_len):
    w_list[ord(w[i])-65] += 1

cnt = 0 
length = 0
for i in range(g_len):
    length += 1
    sa_list[ord(s[i])-65] += 1

    if length == w_len:
        if sa_list == w_list:
            cnt += 1
        sa_list[ord(s[i-length+1])-65] -= 1
        length -= 1

print(cnt)