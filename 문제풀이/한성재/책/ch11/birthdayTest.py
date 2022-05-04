import random

TRIALS = 100000
same_birthdays = 0

#10만번 실험 진행

for _ in range(TRIALS):
    birthdays = []
    #23 명이 모였을 때, 생일이 같은 경우 same_birthdays += 1
    for i in range(57):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

# 전체 10만번의 실험 중 생일이 같은 실험의 확률
print(f'{same_birthdays / TRIALS*100}%')