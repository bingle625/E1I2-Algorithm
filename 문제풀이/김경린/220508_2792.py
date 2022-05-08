from sys import stdin
import math
student, colorNum = map(int,stdin.readline().split())

colors = []
for i in range(colorNum):
    color = int(stdin.readline())
    colors.append(color)

left = sum(colors)//student
right = max(colors)



def isEnoughJewel(colors,mid,num):
    sum = 0
    for color in colors:
        sum += math.ceil(color/mid)
    if sum > num:
        return False
    else:
        return True
            

while left<right:
    num = student
    mid = left + (right-left)//2
    if isEnoughJewel(colors,mid,num):
        right = mid
    else:
        left = mid + 1

print(right)

