cnt = int(input())
nums = []
for i in range(cnt):
    num = int(input())
    nums.append(num)
nums.sort()

print(*nums,sep='\n')
