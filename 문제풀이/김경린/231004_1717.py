## 1717
from collections import defaultdict
import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
nums_set = defaultdict(int)

for i in range(n+1):
    nums_set[i] = i

for _ in range(m):
    command, n1, n2 = map(int,sys.stdin.readline().rstrip().split(' '))
    if command == 0:
        while n2 != nums_set[n2]:
            n2 = nums_set[n2]

        while n1 != nums_set[n1]:
            n1 = nums_set[n1]

        if n1 < n2:  
            nums_set[n1] = n2
        else:
            nums_set[n2] = n1

    
    else:
        if n1 == n2:
            print('yes')
        else:
            while nums_set[n1] != n1:
                n1 = nums_set[n1]
            while nums_set[n2] != n2:
                n2 = nums_set[n2]

            print('no' if n1!=n2 else 'yes')
