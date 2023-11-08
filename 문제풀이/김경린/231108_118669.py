from collections import defaultdict, deque
import heapq

def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)
    
    for path in paths:
        i, j, w = path
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    min_intensity = 10000001
    min_summit = 0
    
    weights = []
    visited = [ 10000001 for _ in range(n+1)]
    for summit in summits:
        visited[summit] = 0
        for i, w in graph[summit]:
            heapq.heappush(weights, (w, summit, i))
            if i not in gates:
                visited[i] = w

   

    while len(weights) > 0:
        # print(weights, visited)
        w, summit, i = heapq.heappop(weights)
        
        if w >= min_intensity:
            break
            
        if visited[i] < w:
            continue
      
        if i in gates:
            if min_intensity > w:
                min_intensity = w
                min_summit = summit
                continue
        for j, new_w in graph[i]:
            max_w = max(w, new_w)
            if j not in summits and visited[j] > max_w:
                visited[j] = max_w
                heapq.heappush(weights, (max_w, summit, j))
    
        
    return [min_summit, min_intensity]