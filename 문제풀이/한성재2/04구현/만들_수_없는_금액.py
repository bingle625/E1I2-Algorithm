number = int(input())
 
numbers = list(map(int, input().split()))

numbers.sort()

target = 1

for elem in numbers:
    if elem > target:
        break
    else:
        target = target + elem

print(target) 