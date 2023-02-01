#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
# 




def biggerIsGreater(w):
    w = list(w)
    for i in range(len(w)-1, 0, -1):
        if w[i] > w[i-1]:
            target = i-1
            last = w[target+1: ]
            last.sort()
            for j in range(len(last)):
                if last[j] > w[target]:
                    f = last[j]
                    last[j] = w[target]
                    
                    return ''.join(w[:target] + [f] + last)
    return "no answer"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
