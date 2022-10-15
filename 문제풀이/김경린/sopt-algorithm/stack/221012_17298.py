
from sys import stdin
nums_len = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().split()))

nge = [ -1 for _ in range(nums_len)]
tmp = []
for i in range(len(nums)):
    while len(tmp) and nums[i]>tmp[-1][0]:
        idx = tmp.pop()[1]
        nge[idx] = nums[i]
    tmp.append((nums[i],i))

for i in range(len(nge)):
    print(nge[i], end=' ')

