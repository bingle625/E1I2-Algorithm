# 네트워크 딜레이타임

import collections
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        # 큐 변수: [(소요시간, 정점)]
        Q =[(0,k)]
        dist = collections.defaultdict(int)
        
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q,(alt,v))
                    
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1