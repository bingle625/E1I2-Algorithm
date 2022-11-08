def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    avail_list = []
    
    for i in range(len(words)):
        current = words[i]
        avail_list.append(current)
        for j in range(len(words)):
            if i == j:
                continue
            current += words[j]
            avail_list.append(current)
            for k in range(len(words)):
                if k == i or k == j:
                    continue
                current += words[k]
                avail_list.append(current)
                for l in range(len(words)):
                    if l == i or l == j or l == k:
                        continue
                        avail_list.append(current + words[l])
    
    for elem in babbling:
        if elem in avail_list:
            answer += 1
    
    return answer

def cases(string):
    