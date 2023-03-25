def min_solar(start_x, start_y, fin_x, fin_y):
    planet_num = int(input())
    cnt = 0
    for i in range(planet_num):
        x, y, r = map(int, input().split())
        start_planet_len = (start_x-x)**2 + (start_y-y)**2
        fin_planet_len = (fin_x-x)**2 + (fin_y-y)**2
        if (start_planet_len < r**2)^(fin_planet_len < r**2):
            cnt += 1
    return cnt
    

case = int(input())

for i in range(case):
    start_x, start_y, fin_x, fin_y = map(int, input().split(' '))
    min_cnt = min_solar(start_x, start_y, fin_x, fin_y)
    print(min_cnt)
