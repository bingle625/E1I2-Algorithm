# 구름
from collections import deque
cnt = int(input())
hamburgers = deque(map(int, input().split(' ')))

i = 0
def is_nice(hamburgers):
	sum_of_value = 0
	max_val = max(hamburgers)
	prev = 0
	is_increase = True
	for h in hamburgers:
		if h == max_val:
			if not is_increase and prev < max_val:
				return 0
			is_increase = False
			prev = h
			continue
		if is_increase:
			if h < prev:
				return 0
		elif not is_increase:
			if h > prev:
				return 0
		
		prev = h

	return sum(hamburgers)
answer = is_nice(hamburgers)
print(answer)
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
