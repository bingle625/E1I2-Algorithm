#2609 최대공약수와 최소공배수

a , b = map(int, input().split())

maxR = 1
for num in range(1,min(a,b)+1):
    if a % num == 0 and b % num == 0:
        maxR = num
    
print(maxR)
print(maxR*(a//maxR)*(b//maxR))