import collections


N,M = map(int,input().split())

kgs= collections.Counter(list(map(int,input().split()))).most_common()

total = N*(N-1) // 2
minus = 0

for elem in kgs:
    minus += elem[1]*(elem[1]-1) //2

print(total-minus)