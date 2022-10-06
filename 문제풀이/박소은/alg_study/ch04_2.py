
n = int(input())

total = (n+1)*6*10*6*10 # 전체 경우의 수

# xx분 xx초에 3이 하나라도 포함이 안 될 경우
no3 = n*5*9*5*9

if n < 3:
    print(total - no3)
else:
    print(total - n*5*9*5*9)