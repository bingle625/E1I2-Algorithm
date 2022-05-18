
from itertools import combinations
from math import comb
from sys import stdin

def strToBin(word):
    strsBin = 0
    for i in range(len(word)):
        strsBin = strsBin | 1<<ord(word[i])-ord('a')

    return strsBin

n, k = map(int, stdin.readline().rstrip().split())
alpha = 0
alpha = alpha | (1 << ord('a')-ord('a'))
alpha = alpha | (1 << ord('t')-ord('a'))
alpha = alpha | (1 << ord('n')-ord('a'))
alpha = alpha | (1 << ord('i')-ord('a'))
alpha = alpha | (1 << ord('c')-ord('a'))


strsSet = []
strs = []
maxNum = 0

for i in range(n):
    tmp = stdin.readline().rstrip()
    strs.append(strToBin(tmp[4:-4]))
    
if k < 5 :
    print(0)

else:
    availAlpha = [2,4,5,6,7,8,10,11,12,13,15,16,17,18,19,21,22,23,24,25,26]
    for idxs in list(combinations(availAlpha,k - 5)):
        
        for idx in idxs:
            alpha = alpha | (1<<idx-1)
        cnt = 0
        for word in strs:
            if alpha & word == word:
                cnt += 1
        maxNum = max(maxNum, cnt)

        for idx in idxs:
            alpha = alpha ^ (1<<idx-1)
    


    print(maxNum)



