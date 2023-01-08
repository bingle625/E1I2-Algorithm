from sys import stdin

# def least_common_multiple(x, y):
#     for i in range(max(x,y),x*y+1):
#         if i % x == 0 and i % y == 0:
            # return i
def find(m, n, year_x, year_y):
    share = 0
    least_multiple = m*n
    standard = max(m, n)
    if standard==m:
        standard_year = year_x
        comp = n
        comp_year = year_y
    else:
        standard_year = year_y
        comp = m
        comp_year = year_x
    while True:
        num = standard*share+standard_year
        if standard*share >= least_multiple:
            return -1
        else:
            if (num - comp_year)%comp==0:
                return num
            else:
                share+=1
case = int(stdin.readline())
for i in range(case):
    m, n, year_x, year_y = map(int, stdin.readline().rstrip().split())

    print(find(m,n,year_x, year_y))

