# N: 남은 근무 일수
import collections

N = int(input())
time = [0]  # 1일부터 시작하기 위해 0번째 dummy값 넣기
price = [0]
for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dict = collections.defaultdict(int) # max price를 저장하는 dict

# N일부터 1일까지 역순으로
for i in range(N, 0, -1):
    if i+time[i]-1 <= N:    # N일 안에 할 수 있는 상담인 경우
        # i==2일 때: dict[3]=45인 값을 유지할 것인가 vs price[2]를 받을 것인가
        dict[i] = max(dict[i+1], price[i]+dict[i+time[i]])
    else:
        dict[i] = dict[i+1]

print(dict[1])