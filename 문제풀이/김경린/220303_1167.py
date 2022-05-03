
from collections import defaultdict
import sys 
sys.setrecursionlimit(10**5)

#1967 인터넷 풀이 활용 

node_num = int(input())

tree = [[] for _ in range(node_num+1)]

visited = [0 for _ in range(node_num+1)]

distance = [-1 for _ in range(node_num+1)]

for i in range(node_num):
    input_list = list(map(int,input().split()))
    head_node = input_list[0]
    for i in range(1,len(input_list)-1):
        tree[head_node].append(input_list[i])

def dfs(cur_node,weight):
    for i in range(len(tree[cur_node])//2):
        next_node = tree[cur_node][2*i]
        next_weight = tree[cur_node][2*i+1]
        if distance[next_node]==-1:
            distance[next_node] = weight+next_weight
            dfs(next_node,distance[next_node])

distance[1] = 0
dfs(1,0)
#거리가 가장 먼 노드

start = distance.index(max(distance))
distance = [-1 for _ in range(node_num+1)]
distance[start] = 0
dfs(start,0)
print(max(distance))
