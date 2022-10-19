# BFS는 큐 자료구조를 이용하는 것이 가장 정석적
# 먼저 들어온 것이 먼저 나가게 되어, 가장 가까운 노드부터 탐색을 진행하게 됨
# 일반적으로 시간 복잡도는 DFS와 비슷하나, 컴퓨팅 속도에서 BFS가 더 빠르다는 것을 알고 있으면 된다.

# BFS 메서드 정의
from collections import deque


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
