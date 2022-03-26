from sys import stdin

N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))

A = sorted(A,reverse=True)
B = sorted(B)

sum = 0

for i in range(len(A)):
    sum += A[i]*B[i]
print(sum)