from typing import List

minute, second = input().split(':')
second = int(second) + int(minute) * 60
count, start = 0, 0

while second > 0:
    count += 1
    if second >= 600:
        second -= 600
    elif second >= 60:
        second -= 60
    elif second >= 30:
        if start == 0:
            start = 1
        second -= 30
    else:
        second -= 10
    
if second == 0 and start == 0:
    count += 1

print(count)