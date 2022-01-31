
def dfs(graph, start_node, cnt):
    stack = list()
    visit = list()
    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node >= 0 and node < M:
            cnt += 1
            visit = list()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return cnt


N, M = input().split()
N = int(N)
M = int(M)
board = [[int(x) for x in input().split()]for y in range(N)]

glass = {}
for height in range(N):
    for width in range(M):
        if board[height][width] == 1:
            strong = []
            for i in dx:
                if width+dx[i] >= 0 and width+dx[i] < M and height-1 < N and height-1 >= 0:
                    if board[height-1][width+dx[i]] == 1:
                        strong.append(
                            (height-1)M+width+dx[i])
            glass[Mheight+width] = strong
cnt = 0
for key in glass:
    if key >= (N-1)M and key < NM:
        cnt = dfs(glass, key, cnt)
print(cnt % 1000000007)
