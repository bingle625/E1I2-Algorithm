# 숫자의 합


# case = int(input())

# temp = input()
# nums = list(map(int, temp))

# print(sum(nums))

# 2번째 풀이 숫자의 개수 활용

case = int(input())

temp = input()
sum = 0
for i in range(case):
    sum += int(temp[i])
print(sum)
