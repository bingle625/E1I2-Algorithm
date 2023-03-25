from collections import deque
from sys import stdin

def ac(arr, command):
    command_idx = 0
    reverse = 0
    while command_idx < len(command):
        if command[command_idx] == 'R':
            reverse += 1
        else:
            if reverse%2==0:
                arr.popleft()
            else:
                arr.pop()
        command_idx += 1
    if reverse%2==1:
        arr.reverse()
    ans = "[" + ",".join(list(arr)) + "]"
    return ans



case = int(stdin.readline())

for i in range(case):
    command = stdin.readline().rstrip()
    arr_len = int(stdin.readline())
    arr = stdin.readline().rstrip()
    if command.count('D') > arr_len:
        print('error')
    else:
        if arr_len>0:
            arr = arr[1:-1].split(',')
        else:
            arr = ''
        print(ac(deque(arr), command))


# 굳이 arr의 원소를 int로 바꿀 필요 없음
# 연속된 'R'에 대해서만 한번에 계산하도록하면 시간초과 => 전체 'R'의 개수