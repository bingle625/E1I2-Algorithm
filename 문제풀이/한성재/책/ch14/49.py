

import collections


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        # 왜 range(n+1)일까
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves
