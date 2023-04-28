# 프로그래머스 92343
from collections import defaultdict

def solution(info, edges):
    global max_sheep
    max_sheep = 1

    graph = defaultdict(list)
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    def dfs(cur, sheep, wolf):
        global max_sheep
        
        for i in range(len(info)):
            if info[i] == -1:
                for j in graph[i]:
                    if (info[j] == 1 and wolf+1 < sheep):
                        info[j] = -1
                        dfs(j, sheep, wolf +1)
                        info[j] = 1
                    elif info[j] == 0: 
                        print(j)
                        max_sheep = max(max_sheep, sheep+1)
                        info[j] = -1
                        dfs(j, sheep+1, wolf)
                        info[j] = 0
    info[0] = -1
    dfs(0, 1, 0)

    answer = max_sheep
    
    return answer

# 최대 몇마리의 양을 모을 수 있는지
# 방문했던 곳 들릴 수 있음 0-2-5-1을 어케 처리하지 루프 안돌도록
# dict[방문했던 곳] 다시 가서 같은 활동 ㄱㄱ 그렇다면 dfs? 
# max를 계속 저장하면서 돌아 다님
