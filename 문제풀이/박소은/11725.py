from typing import List
import collections

def find_tree(Tree, n: int) -> List:
    t = collections.defaultdict(list)

    for key, value in Tree.items():
        for elem in value:     
            if elem in t:       # 키 있는지 탐색
                t[elem].append(key)
            else:
                t[key].append(elem)

    result = []
    for i in range(2, n + 1):
        for k, v in t.items():
            if i in v:
                result.append(k)

    return result

# 입력
n = (int)(input())
Tree = collections.defaultdict(list)
for i in range(n - 1):
    x, y = map(int, input().split())
    Tree[x].append(y)

print(*find_tree(Tree, n), sep='\n')