# n = int(input())
# clients = []
# for i in range(n):
#     age, name = input().split(' ')
#     clients.append((age,name,i))

# clients.sort(key=lambda x: (int(x[0]), x[2]))

# for age, name, i in clients:
#     print(age + ' ' + name+' ')


## 5568
from itertools import permutations

n = int(input())
k = int(input())

nums = []
for i in range(n):
    num = input()
    nums.append(num)

result = list(permutations(nums, k))
for i in range(len(result)):
    result[i] = ''.join(result[i])

result = set(result)

print(len(result))

    

    

    



