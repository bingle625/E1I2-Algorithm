size = int(input())

video = [ [0 for _ in range(size)] for _ in range(size)]

for y in range(size):
    video[y] = list(map(str, input().split()))

def isSame(startX, finishX, startY, finishY):
    num = video[startY][startX]
    for x in range(startX, finishX+1):
        for y in range(startY, finishY + 1):
            if video[y][x]!=num:
                return False
    return True

def compress()
