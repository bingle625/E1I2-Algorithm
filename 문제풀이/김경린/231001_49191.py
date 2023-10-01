from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    for result in results:
        winner, loser = result[0], result[1]
        win[winner].add(loser)
        lose[loser].add(winner)
 
    
    for i in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        visited[i] = 1
        deq = deque()
        deq.append(i)
        cnt = 0
        while len(deq):
            node = deq.popleft()
            for w in win[node]:
                if not visited[w]:
                    deq.append(w)
                    visited[w] = 1
                    cnt += 1
        deq = deque()
        visited = [0 for _ in range(n+1)]
        visited[i] = 1
        deq.append(i)
        while len(deq):
            node = deq.popleft()
            for l in lose[node]:
                if not visited[l]:
                    deq.append(l)
                    visited[l] = 1
                    cnt += 1
        if cnt == n-1:
            answer += 1
                
        
    
    return answer