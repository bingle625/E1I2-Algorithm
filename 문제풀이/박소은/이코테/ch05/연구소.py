# p.341 16. 연구소
# 연구소 크기: N*M, 새로 세울 수 있는 벽은 3개
# 아이디어: 모든 경우의 조합을 BFS로 탐색하면서 안전 구역을 탐색해보자.
from collections import deque
import copy

# 입력 받기
N, M = map(int, input().split())    # 세로 N, 가로 M
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

temp = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]  # 상우하좌

# safe area 크기 계산 메서드
def calSafeArea(graph):
    area = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                area += 1
    return area

# 바이러스 퍼뜨리는 메서드: DFS 사용
def virus(temp):
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                for k in range(4):
                    x, y = i+dx[k], j+dy[k] # 상하좌우 이동
                    if x >= 0 and x < N and y >= 0 and y < M and temp[x][y] == 0:
                        temp[x][y] = 2
    return temp

# TODO: 모든 조합 구하기, virus 전파 수정

# BFS로 모든 경우의 조합 테스트해보기
def bfs():
    wallCnt = 0 # 세운 벽의 개수
    answer = 0  # 안전구역의 최댓값

    for i1 in range(N):
        for j1 in range(M):
            graph[i1][j1] = (1 if graph[i1][j1] == 0 else graph[i1][j1])    # 벽 1개 세움

            for i2 in range(i1, N):
                for j2 in range(j1, M):
                    graph[i2][j2] = (1 if graph[i2][j2] == 0 else graph[i2][j2])    # 벽 2개 세움

                    for i3 in range(i2, N):
                        for j3 in range(j2, M):
                            graph[i3][j3] = (1 if graph[i3][j3] == 0 else graph[i3][j3])    # 벽 3개 세움
                            temp = virus(copy.deepcopy(graph)) # 바이러스 퍼짐
                            safeArea = calSafeArea(temp)

                            if safeArea > answer:
                                answer = safeArea
                                printGraph(temp)

                            graph[i3][j3] = 0    # 3번째 벽 허물기
                    graph[i2][j2] = 0    # 2번째 벽 허물기
            graph[i1][j1] = 0    # 3번째 허물기
    print(answer)


def printGraph(graph):
    for i in range(N):
        print(graph[i], sep=" ")
    print("\n")

bfs()
