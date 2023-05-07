from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    global cost, graph
    
    def dijkstra(target,s):
        global cost, graph
        
        dist = [ float('inf') for _ in range(n+1) ]
        dist[s] = 0
        for node in graph[s]:
            heapq.heappush(target, (cost[s][node], node))
            dist[node] = cost[s][node]

        while len(target):
            min_dist, min_node = heapq.heappop(target)
            if min_dist > dist[min_node]:
                continue
            
            for node in graph[min_node]:
                if dist[node] > min_dist + cost[min_node][node]:
                    dist[node] = min_dist + cost[min_node][node]
                    heapq.heappush(target, (dist[node], node))
        return dist
    
    
    answer = 0
    graph = defaultdict(list)
    cost = [ [0 for _ in range(n+1)] for _ in range(n+1) ]
    for fare in fares:
        graph[fare[0]].append(fare[1])
        graph[fare[1]].append(fare[0])
        cost[fare[0]][fare[1]] = fare[2]
        cost[fare[1]][fare[0]] = fare[2]
    
    with_a_b = dijkstra([], s)
    
    result = [0 for _ in range(n+1)]
    
    for start in range(1, n+1):
        each = dijkstra([], start)
        result[start] = with_a_b[start] + each[a] + each[b]

        
    result = result[1:]
    return min(result)






# 프로그래머스 72413번