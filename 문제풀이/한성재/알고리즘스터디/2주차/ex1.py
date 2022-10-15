max = int(input())

trail = list(input().rstrip().split())

cod = [1, 1]

side_arrow = {'R': 1, 'L': -1, }
up_arrow = {'U': -1, 'D': 1}

for elem in trail:
    if elem in side_arrow:
        if cod[1] + side_arrow[elem] < 1 or cod[1] + side_arrow[elem] > max:
            pass
        else:
            cod[1] += side_arrow[elem]
    else:
        if cod[0] + up_arrow[elem] < 1 or cod[0] + up_arrow[elem] > max:
            pass
        else:
            cod[0] += up_arrow[elem]

print(cod)
