# 빗물 트래핑

from turtle import left


def waterFalls(heights: list) -> int:

    volume = 0
    for i in range(len(heights)):
        left_max = 0
        right_max = 0
        for k in range(0, i):
            if(heights[k] > left_max):
                left_max = heights[k]

        for k in range(i+1, len(heights)):
            if(heights[k] > right_max):
                right_max = heights[k]

        mini = min(left_max, right_max)
        if(mini-heights[i] < 0):
            continue
        else:
            volume += mini-heights[i]

    return volume


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(waterFalls(heights))
