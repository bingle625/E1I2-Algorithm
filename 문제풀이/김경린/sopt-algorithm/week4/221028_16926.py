from sys import stdin




n, m, r = map(int,stdin.readline().strip().split())

arr = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]




for t in range(r):
    rectangle_num = min(n, m)//2
    for i in range(rectangle_num):
        x, y = i, i
        temp = arr[x][y]
                            # 안쪽까지 계속 고려해야하기 때문에 n-i랑 m-i까지로 범위설정
        for j in range(i + 1, n - i):  #좌
            x = j
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  #하
            y = j
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value

        for j in range(i + 1, n - i):  #우
            x = n - j - 1
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  #상
            y = m - j -1
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
            


for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end = ' ')
    print('')
