# def complement(num: str):
#     tmp = []
#     for i in range(len(num)):
#         if num[i] == '0':
#             tmp.append('1')
#         elif num[i] == '1':
#             tmp.append('0')

#     tmp = int("".join(tmp), 2)+1
#     return tmp


# def binary(num):
#     tmp = bin(num)
#     tmp = list(str(tmp))[2:]
#     for i in range(32-len(tmp)):
#         tmp.insert(0, '0')
#     return tmp


# def compare_bin(num1, num2):
#     cnt = 0
#     for i in range(len(num1)):
#         if num1[i] != num2[i]:
#             cnt += 1
#     return cnt


# num = int(input())
# bin_num = binary(num)
# comple_num = complement(bin_num)
# comple_bin_num = binary(comple_num)
# print(compare_bin(comple_bin_num, bin_num))

# from sys import stdin

# dx = [-1, 0, 1]


# def dfs(graph, start_node, cnt):
#     stack = list()
#     visit = list()
#     stack.append(start_node)

#     while stack:
#         node = stack.pop()

#         if node >= 0 and node < M:
#             cnt += 1
#             visit = list()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])
#     return cnt


# N, M = stdin.readline().split()
# N = int(N)
# M = int(M)
# board = [[int(x) for x in stdin.readline().split()]for y in range(N)]

# glass = {}
# for height in range(N):
#     for width in range(M):
#         if board[height][width] == 1:
#             strong = []
#             for i in dx:
#                 if width+dx[i] >= 0 and width+dx[i] < M and height-1 < N and height-1 >= 0:
#                     if board[height-1][width+dx[i]] == 1:
#                         strong.append(
#                             (height-1)*M+width+dx[i])
#             glass[M*height+width] = strong
# cnt = 0
# for key in range((N-1)*M, N*M):
#     if key in glass and key >= (N-1)*M and key < N*M:
#         cnt = dfs(glass, key, cnt)
# print(cnt % 1000000007)
import math

N, S = map(int, input().split())

good_num = (S-1)*(2*N)//(5*math.pow(10, 9))
done = 1
score = good_num*5*(math.pow(10, 9))//(2*N)
if score > S:
    while True:
        good_num -= 1
        if good_num == 0:
            done = 0
            break
        score = good_num*5*(math.pow(10, 9))/(2*N)
        if score == S:
            print(S)
elif score < S:
    while True:
        good_num += 1
        score = good_num*5*(math.pow(10, 9))//(2*N)
        if score > S:
            done = 0
            break
        if score == S:
            print(S)
else:
    print(S)
if done == 0:
    print(-1)
