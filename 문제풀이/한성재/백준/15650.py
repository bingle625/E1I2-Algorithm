# N과 M (2)


num_list = list(map(int, input().split()))

N = num_list[0]
M = num_list[1]

result = []


def dfs(elements: list, start: int, n: int, m: int):

    if m == 0:
        result.append(elements[:])

    for i in range(start, n+1):
        elements.append(i)
        dfs(elements, i+1, n, m-1)
        elements.pop()


dfs([], 1, N, M)

for elem in result:
    print(" ".join(str(_) for _ in elem))
