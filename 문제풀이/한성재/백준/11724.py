# 11724번


marked = []
dic = {}


def iterative_dfs(discovered: list, start_v: int):
    if start_v in discovered:
        return discovered
    else:
        stack = [start_v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in dic[v]:
                    stack.append(w)
        return discovered


N, M = map(int, input().split())

for i in range(M):
    u, v = map(int, input().split())

    if u not in dic:
        dic[u] = [v]
    else:
        dic[u].append(v)

    if v not in dic:
        dic[v] = [u]
    else:
        dic[v].append(u)

discovered = []
cnt = 0

for i in range(1, N+1):
    if i not in discovered:
        cnt += 1
    discovered = iterative_dfs(discovered, i)

print(cnt)
