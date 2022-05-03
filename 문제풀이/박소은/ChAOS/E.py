import sys

con_building = []
count = 0
lecture_num, building_num = map(int, sys.stdin.readline().split())

for elem in range(building_num):
    b1, b2 = map(int, sys.stdin.readline().split())
    temp = 0

    for building in con_building:
        if b1 in building or b2 in building:
            building.update({b1, b2})
            temp = 1

    if temp == 0:
        con_building.append({b1, b2})
    temp = 0

timetable = list(map(int, sys.stdin.readline().split()))
prev = timetable[0]

for i in timetable[1:]:
    for building in con_building:
        if (prev in building and i in building):
            temp = 1
            break
    if temp == 0:
        count += 1
    temp = 0
    prev = i

print(count)
