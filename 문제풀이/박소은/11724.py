import collections
import sys
sys.setrecursionlimit(100000)

def g_search(graph) -> int:
    link = []   # 연결 요소
    visited = set()     # 방문한 노드

    def dfs(vertex, l_set):
        if vertex not in visited:
            visited.add(vertex)
            l_set.add(vertex)
            if len(l_set) == 1:
                link.append(l_set)
            
        
        for w in graph[vertex]:
            if w not in visited:
                l_set = dfs(w, l_set)
            elif w in visited and w not in l_set:
                for elem in link:
                    if w in elem:
                        elem |= l_set # 집합 결합
                        temp = l_set
                        if l_set in link:
                            link.remove(l_set)
                        return temp
        return l_set
            
    
    for x in list(graph):
        dfs(x, set())

    return len(link)
            

# 입력
n, m = map(int, input().split())
graph = collections.defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

print(graph)
print(g_search(graph))