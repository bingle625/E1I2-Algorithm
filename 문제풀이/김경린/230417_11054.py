def binary_search(target, target_list):
    start = 0
    finish = len(target_list)

    while start < finish:
        idx = (start+finish)//2
        if target_list[idx] < target:
            start = idx + 1
        elif target_list[idx] > target:
            finish = idx
        else:
            return idx
    return finish

n = int(input())

nums = list(map(int, input().split()))

#    10 20 10 30 20 50
answer = [0]

for num in nums:
    if answer[-1] < num:
        answer.append(num)
    else:
        idx = binary_search(num, answer)
        answer[idx] = num
print(len(answer)-1)

# 이분 탐색에서 idx를 return하는 것이 아니라 
# 큰 쪽인 finish를 return해야함 