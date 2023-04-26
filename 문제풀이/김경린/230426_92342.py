# 프로그래머스 92342


max_score = 0
win_info = []
max_list = []
enemy_info = []
def dfs(n, i, visited, score, enemy_score):
    global max_score, max_list, enemy_info
    
    if i != -1:
      visited[i] = 1
    if n == 0:
        if max_score <= score-enemy_score:
            max_score = score-enemy_score
            max_list = visited[:]
        return 
    
    for j in range(i+1, len(visited)):
        if not visited[j] and n-win_info[j] >= 0:
            dfs(n-win_info[j], j, visited, score + 10-j, enemy_score - (10-j) if enemy_info[j] else enemy_score)
            visited[j] = 0
         
def solution(n, info):
    global win_info, enemy_info
    answer = []
    enemy_info = info
    win_info = [ x+1 for x in info]
    visited = [0 for _ in range(len(info))]
    enemy_score = 0
    for i in range(len(info)):
      enemy_score += (1 if info[i] else 0)*(10-i)
    dfs(n, -1, visited, 0, enemy_score)
    if len(max_list) == 0:
        answer = [-1]
    else:
        for i in range(len(win_info)):
            answer.append(max_list[i]*win_info[i])
    return answer


# 정답
# def solution(n, info):
#     global answer, max_score
#     answer = []
#     max_score = 0
    
#     def score(ryan):
#         scores = 0
#         for i in range(11):
#             if ryan[i] == 0 and info[i] == 0:
#                 continue
#             elif ryan[i] <= info[i]:
#                 scores -= 10-i
#             else:
#                 scores += 10-i
#         return scores
    
#     def dfs(idx, arrow, ryan):
#         global answer, max_score
#         if idx == -1 and arrow:
#             return
#         if arrow == 0:
#             scores = score(ryan)
#             if max_score < scores:
#                 max_score = scores
#                 answer = ryan[:]
#             return
#         for i in range(arrow,-1,-1):
#             ryan[idx] = i
#             dfs(idx-1, arrow-i, ryan)
#             ryan[idx] = 0
#     dfs(10, n, [ 0 for _ in range(11)])
    
#     return answer if max_score != 0 else [-1]