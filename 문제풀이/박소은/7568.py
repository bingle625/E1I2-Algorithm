
num = int(input())
peoples = []

for i in range(num):
    peoples.append(tuple(map(int, input().split())))

for people in peoples:
    ranking = 1

    for compare in peoples:
        if (people[0] < compare[0]) & (people[1] < compare[1]):
            ranking += 1
    print(ranking, end = ' ')