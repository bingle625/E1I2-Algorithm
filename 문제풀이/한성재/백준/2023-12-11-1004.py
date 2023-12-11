# 어린 왕자 1004번
import sys


def is_circle_in_and_out(c_x, c_y, r, x, y, a, b):
    first = (x - c_x) ** 2 + (y - c_y) ** 2 - r ** 2
    second = (a - c_x) ** 2 + (b - c_y) ** 2 - r ** 2

    return first * second < 0


def get_minimum_path(circle_num, x, y, a, b):
    cnt = 0
    for i in range(circle_num):
        c_x, c_y, r = map(int, sys.stdin.readline().split())
        if is_circle_in_and_out(c_x, c_y, r, x, y, a, b):
            cnt += 1
    return cnt


def solve_case():
    x, y, a, b = map(int, sys.stdin.readline().split())
    circle_num = int(sys.stdin.readline())
    print(get_minimum_path(circle_num, x, y, a, b))


def solve_problem():
    test_case_num = int(sys.stdin.readline())
    for i in range(test_case_num):
        solve_case()


solve_problem()
