def solution(N, road, K):
    answer = 0
    graph = {}

    for _ in range(len(road)):
        graph[road[0]] = road[1]
        graph[road[1]] = road[0]
    
    print(graph)

    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)