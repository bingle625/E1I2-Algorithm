import heapq

n, k = map(int, input().split(' '))
fruits = []
for i in range(n):
	p, c = map(int, input().split(' '))
	heapq.heappush(fruits, (-c//p, p))

answer = 0
while len(fruits) and k > 0:
	val, p = heapq.heappop(fruits)
	if k - p >= 0:
		answer -= val*p
		k -= p
	else:
		answer -= val*k
		k = 0
print(answer)
	