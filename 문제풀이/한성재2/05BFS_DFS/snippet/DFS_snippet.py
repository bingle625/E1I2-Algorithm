# DFS 메서드 정의
# 최대한 멀리 있는 노드를 우선으로 탐색하는 방식
# 일반적으로, 스택을 이용하여 구현하며,
# 재귀적 방식의 경우, 그 메커니즘이 애초에 스택과 상당히 유사하기 때문에, 재귀적 방식을 사용하기도 한다.
from calendar import c


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결돈 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 그래프, 인접 리스트 방식
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
