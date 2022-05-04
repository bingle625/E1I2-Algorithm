#2533번 사회망 서비스(SNS)

import collections
import sys


ourTree = collections.defaultdict(list)
earlyAdopted = []

nodeNum = int(input())

for _ in range(nodeNum-1):
    par,chil = map(int,sys.stdin.readline().split())
    
    if ourTree[par]:
        ourTree[par].append(chil)
    else:
        ourTree[par] = [chil]

def fs(node):
    for child in ourTree[node]:
        if node not in earlyAdopted:
            if child not in ourTree:
                earlyAdopted.append(node)
        fs(child)

fs(1)
print(len(earlyAdopted))