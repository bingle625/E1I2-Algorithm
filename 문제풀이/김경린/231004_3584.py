# ## 3584
# from collections import defaultdict, deque

# case = int(input())

# for i in range(case):
#     n = int(input())
#     parent = defaultdict(int)
#     child = defaultdict(list)
#     depth = defaultdict(int)

#     for j in range(n-1):
#         p,c = map(int, input().split(' '))
#         parent[c] = p
#         child[p].append(c)

#     for j in range(1, n+1):
#         if parent[j] == 0:
#             root = j
#             break
    
#     visited= deque()
#     visited.append((root, 0))
#     depth[root] = 0
#     while len(visited):
#         node, dep = visited.popleft()
#         for c in child[node]:
#             visited.append((c, dep+1))
#             depth[c] = dep+1
    

#     node1, node2 = map(int, input().split(' '))
#     while node1 != node2:
#         if depth[node1] > depth[node2]:
#             node1 = parent[node1]
#         else:
#             node2 = parent[node2]
    
#     print(node1)