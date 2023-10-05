from collections import defaultdict
import sys
t = int(input())

for _ in range(t):
    w = input()
    k = int(input())
    
    char_dict = defaultdict(list)
    for idx,c in enumerate(w):
        char_dict[c].append(idx)
    
    max_length = -sys.maxsize
    min_length = sys.maxsize
    for key in char_dict.keys():
        if len(char_dict[key]) >= k:
            for i in range(len(char_dict[key])-k+1):
                length = char_dict[key][i+k-1] - char_dict[key][i] + 1
                max_length = max(max_length, length)
                min_length = min(min_length, length)
    

    if max_length == -sys.maxsize:
        print(-1)
    else:
        print(min_length, end=' ')
        print(max_length)



