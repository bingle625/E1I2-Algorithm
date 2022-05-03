# 그래프 (인접리스트 방법)
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# # 1. recursive한 방법


# def recursive_dfs(v, discovered=[]):
#     discovered.append(v)
#     for w in graph[v]:
#         if w not in discovered:
#             discovered = recursive_dfs(w, discovered)
#     return discovered

# print(recursive_dfs(1))


# 2. stack을 이용한 방법

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


print(iterative_dfs(1))
