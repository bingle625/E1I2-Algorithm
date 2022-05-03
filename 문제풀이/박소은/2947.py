from typing import List

def print_list(l: List):
    for elem in l:
        print(elem, end=' ')
    print()

def switch_wood(w_list: List):
    correct = [n for n in range(1, 5 + 1)]

    while True:
        for i in range(len(w_list) - 1):
            if w_list[i] > w_list[i + 1]:
                w_list[i], w_list[i + 1] = w_list[i + 1], w_list[i]
                print_list(w_list)
        
        if w_list == correct:
            return w_list


w_list = list(map(int, input().split()))
switch_wood(w_list)