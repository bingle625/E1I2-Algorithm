# N: senior citizens#
# M: channel# (1~M개의 채널)
# 어르신이 싫어하는 채널 -> 채널 변경
# 총 채널 변경 횟수는?

from collections import defaultdict

def DFS(root):
    visited = []
    count = 0

    while True:
        if root in visited: # 영원히 안 끝남
            return -1
        else:
            if not dislikeChannels[root]:   # 현재 채널을 싫어하는 사람이 없는 경우
                return count
            else:
                visited.append(root)
                root = likeSeniors[dislikeChannels[root][0]]    # 최연소 senior가 좋아하는 채널
                count += 1

N, M, P = map(int, input().split()) # P: initial channel
likeSeniors = dict()    # likeSeniors[seniorID] = 해당 senior이 좋아하는 채널ID
dislikeChannels = defaultdict(list) # dislikeChannels[채널ID] = [싫어하는 사람들 list]

for i in range(1, N+1):
    likeChannel, dislikeChannel = map(int, input().split())
    likeSeniors[i] = likeChannel
    dislikeChannels[dislikeChannel].append(i)

# 나이 적은 순으로 sorting
for key in dislikeChannels.keys():
    dislikeChannels[key].sort()

print(DFS(P))