from sys import stdin
cnt = int(stdin.readline().strip())

def fib(num):
    if zero[num] != 0 or one[num] != 0:
        return (zero[num],one[num])
    
    bf_num = fib(num-1)
    bf_bf_num = fib(num-2)
    zero[num] = bf_num[0]+bf_bf_num[0]
    one[num] = bf_num[1]+ bf_bf_num[1]
    return (zero[num], one[num])
    
zero = [ 0 for _ in range(41)]
one = [ 0 for _ in range(41)]
zero[0] = 1
one[1] = 1
for i in range(cnt):
    num = int(stdin.readline().strip())
    fib_num = fib(num)
    print(fib_num[0], end = ' ')
    print(fib_num[1])

