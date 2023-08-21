# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

n = int(input())
s = input()

def divide_s(start, cnt, d):
	if cnt == 1:
		d.append(s[start:])
		return
	for i in range(start, n):
		if n-(i+1) >= cnt-1:
			d.append(s[start:i+1])
			divide_s(i+1, cnt -1, d)
max_score = 0
def calc_s(start, cnt, score):
	# print(score)
	global max_score
	if cnt == 1:
		max_score = max(max_score, score + d.index(s[start:]) + 1)
		return
	for i in range(start, n):
		if n-(i+1) >= cnt-1:
			calc_s(i+1, cnt -1, score + d.index(s[start:i+1]) + 1)

d = []
divide_s(0, 3, d)
answer_list = d [-3:]
d = sorted(list(set(d)))
calc_s(0, 3, 0)
print(max_score)