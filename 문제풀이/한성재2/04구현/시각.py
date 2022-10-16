#0959~1006

number = int(input())

temp = 0
for S in range(60):
    if "3" in str(S):
      temp += 1  

cnt = 0
for H in range(number+1):
    if H == 3:
       cnt += 3600
    else:
        for M in range(60):
            if "3" in str(M):
                cnt += 60
            else:
                # 0~ 59까지 3이 포함되는 횟수
                cnt +=  temp

print(cnt)