from sys import stdin

cnt = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
num_sign = list(map(int,stdin.readline().split()))
signs = []

for i in range(4):
    if i==0:
        for j in range(num_sign[i]):
            signs.append('+')

    elif i==1:
        for j in range(num_sign[i]):
            signs.append('-')

    elif i==2:
        for j in range(num_sign[i]):
            signs.append('*')


    elif i==3:
        for j in range(num_sign[i]):
            signs.append('/')

prev_signs = []
results = []


def dfs(signs):
    if len(signs)==0:
        results.append(prev_signs[:])
    for sign in signs:
        next_signs = signs[:]
        next_signs.remove(sign)
        prev_signs.append(sign)
        dfs(next_signs)
        prev_signs.pop()
    

dfs(signs)

#중복 제거를 위해 list를 immutable하도록
results = [tuple(i) for i in results]
results = list(set(results))
cal_results = []

for result in results:
    tmp = nums[0]
    for i in range(1,len(nums)):
        if result[i-1]=='+':
            tmp +=nums[i]
        elif result[i-1]=='-':
            tmp -=nums[i]
        elif result[i-1]=='*':
            tmp *=nums[i]
        elif result[i-1]=='/':
            tmp /=nums[i]
            tmp = int(tmp)

    cal_results.append(tmp)

cal_results.sort()
print(cal_results[-1])
print(cal_results[0])

