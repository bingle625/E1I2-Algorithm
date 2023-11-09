import re

answer = []

def dfs(visited_user, visited_banned, user_id, banned_id, cnt, last_i):
    global answer

    if cnt == len(banned_id):
        answer.append(''.join(visited_user))
        return
    for i in range(last_i, len(user_id)):
        for j in range(len(banned_id)):
            if visited_user[i] == '0' and visited_banned[j] == '0':
                p = re.compile(banned_id[j])
                
                if p.match(user_id[i]):
                    
                    visited_user[i] = '1'
                    visited_banned[j] = '1'
                    dfs(visited_user, visited_banned, user_id, banned_id, cnt+1, i+1)
                    visited_user[i] = '0'
                    visited_banned[j] = '0'

                

def solution(user_id, banned_id):
    num = 0
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace('*', '\w')
        banned_id[i] += '$'
    
    visited_user = ['0' for _ in range(len(user_id))]
    visited_banned = ['0' for _ in range(len(banned_id))]
    dfs(visited_user, visited_banned, user_id, banned_id, 0, 0)
    return len(list(set(answer)))