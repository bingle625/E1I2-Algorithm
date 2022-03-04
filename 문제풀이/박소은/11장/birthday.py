# 생일 문제

import random

TRIALS = 10000
same_birthdays = 0

# 10만 번 실험 진행
for _ in range(TRIALS):
    birthdays = []  # 한 실험 안에서 나온 생일들을 저장
    # 23명이 모였을 때, 생일이 같은 경우 same_brithdays += 1

    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

# 전체 10만 번 실험 중 생일이 같은 실험의 확률
print(f'{same_birthdays / TRIALS * 100}%')
print(birthdays)