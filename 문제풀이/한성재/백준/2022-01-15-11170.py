# 11170번 0의 개수

def find_zero(a: int, b: int) -> int:
    cnt = 0
    for num in range(a, b+1):
        while True:
            if(num % 10 == 0):
                cnt += 1
            num = num // 10
            if num != 0:
                continue
            break
    return cnt


test_num = int(input())

for i in range(test_num):
    n, m = map(int, input().split())
    print(find_zero(n, m))
