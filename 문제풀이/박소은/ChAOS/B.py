import sys

N = int(sys.stdin.readline())
dec = [n for n in range(1, 27 + 1)]

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    left = dec[0:13]
    right = dec[13:27]
    new_dec = []

    right_flag = 1
    for elem in l:
        if right_flag == 1:
            if elem == 1:
                add_elem = [right[0]]
            else:
                add_elem = right[0:elem] 
            right = right[elem:]
            right_flag = 0
        else:
            if elem == 1:
                add_elem = [left[0]]
            else:
                add_elem = left[0:elem]
            left = left[elem:]
            right_flag = 1
        
        new_dec = new_dec + add_elem
    dec = new_dec


index = 1
for i in dec:
    if i == 1:
        print(index)
    index += 1
