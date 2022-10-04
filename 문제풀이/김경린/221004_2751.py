from sys import stdin
cnt = int(stdin.readline())
nums = []
for i in range(cnt):
    num = int(stdin.readline())
    nums.append(num)
nums.sort()

print(*nums,sep='\n')