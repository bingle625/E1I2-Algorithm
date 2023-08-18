from collections import deque, defaultdict
n, k = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

def make_binary(num):
	answer = deque()
	while num > 0:
		answer.appendleft(num%2)
		num = num // 2
	return answer

binary_dict = defaultdict(deque)
for num in nums:
	binary_dict[num] = make_binary(num)

nums.sort(key=lambda x : (-binary_dict[x].count(1), -x))
print(nums[k-1])
	