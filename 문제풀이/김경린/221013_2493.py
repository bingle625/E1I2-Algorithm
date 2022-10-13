from sys import stdin


num = int(stdin.readline().strip())

stack = list(map(int, stdin.readline().split()))


sign = [0 for _ in range(num)]
tmp = []

for i in range(num):
    h = stack.pop()
    while len(tmp) and tmp[-1][0] < h:
        sign[tmp[-1][1]] = num-i
        tmp.pop()
    tmp.append((h, num-i-1))

for i in range(len(sign)):
    print(sign[i], end=' ')
    

