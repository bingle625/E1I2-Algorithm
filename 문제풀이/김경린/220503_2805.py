from sys import stdin

treeNum, target = map(int, input().split())
trees = list(map(int,stdin.readline().split()))
trees.sort()




l = 0
r = trees[-1]

done = 0
while l <= r:
    cut = l + (r-l)//2
    sum = 0
    for tree in trees:
        sum += tree-cut if tree-cut >0 else 0
    if sum >= target:
        l = cut + 1
    elif sum < target:
        r = cut - 1


print(r)
