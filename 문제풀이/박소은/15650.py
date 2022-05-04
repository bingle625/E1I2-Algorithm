from typing import List

# 교과서 풀이
def combine(n: int, m: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], 1, m)
    return results

# n, m = map(int, input().split())
# for e1 in combine(n, m):
#     for e2 in e1:
#         print(e2, end=" ")
#     print()
    

# 반복문 이용
(4, 3) -> 123 124 134 234
def combin(n: int, m: int) -> List[List[int]]:
    results = []
    elements = []
    first = 1

    while first <= n-m+1:
        elements = [first]
        k = first
        while k <= n and len(elements) <= m:
            k += 1
            elements.append(k)
        results.append(elements[:])


    return results

print(combin(4, 2))