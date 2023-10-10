import heapq
# from collections import defaultdict

v, e = map(int, input().split(' '))
parent = [ i for i in range(v+1) ]

def get_parent(n):
    if parent[n] != n:
        parent[n] = get_parent(parent[n])

    return parent[n]


trees = []
for i in range(e):
    tmp = list(map(int, input().split(' ')))
    heapq.heappush(trees, (tmp[2], tmp[0], tmp[1]))

sum_val = 0

while len(trees):
    val, n1, n2 = heapq.heappop(trees)
    n1_parent = get_parent(n1)
    n2_parent = get_parent(n2)
    if n1_parent != n2_parent:
        sum_val += val
        if n1_parent < n2_parent:
            parent[n2_parent] = n1_parent
        else:
            parent[n1_parent] = n2_parent



print(sum_val)