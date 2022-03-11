import sys
sys.setrecursionlimit(10**9)

N = int(input())
dic = dict()
distance = dict()


if N != 0:
    distance[1] = 0

for _ in range(N-1):
    a, b, c = map(int, input().split())

    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)

    distance[b] = c


class sol:
    world_max: int = -sys.maxsize

    def dfs(self, root):
        if root not in distance:
            return 0

        if root not in dic:
            return distance[root]

        max_val = 0
        sec_val = 0
        for elem in dic[root]:
            val = self.dfs(elem)
            if val >= max_val:
                sec_val = max_val
                max_val = val
            elif sec_val <= val <= max_val:
                sec_val = val

        distance[root] = distance[root] + max_val

        self.world_max = max(self.world_max, max_val + sec_val)

        if root != 1:
            return distance[root]
        else:
            return self.world_max


solution = sol()

print(solution.dfs(1))
