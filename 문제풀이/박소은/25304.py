X = int(input())
n = int(input())
total = 0
goods = []
for _ in range(n):
    a, b = map(int, input().split())
    total += a*b

if total == X:
    print("Yes")
else:
    print("No")