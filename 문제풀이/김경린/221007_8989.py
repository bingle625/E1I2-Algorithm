from sys import stdin
def sort_value(x):
    return x[1]
case = int(stdin.readline())
while case:
    times = list(stdin.readline().split())
    times.sort()
    sort_times = []
    for idx in range(len(times)):
        hour,minute = map(int, times[idx].split(":"))
        if hour>=12:
            hour -= 12
        degree = 30*hour + 0.5*minute - 6*minute if 30*hour + 0.5*minute> 6*minute else 6*minute-30*hour - 0.5*minute
        if degree>180:
            degree = 360-degree
        sort_times.append((idx, degree))
    sort_times.sort(key=sort_value)
    idx, degree = sort_times[2]
    print(times[idx])
    case -= 1

