from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline()

p = 'IO'*n + 'I'
cnt = 0
start = 0
answer = 0
while start < m:
    done = 0
    if s[start:start+3] == 'IOI':
        cnt += 1
        start += 2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        start += 1
        cnt = 0
        

        
    

print(answer) 