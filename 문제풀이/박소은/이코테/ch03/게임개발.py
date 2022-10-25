# N * M 직사각형, 각각의 칸은 육지 또는 바다. 동서남북 중 한 곳을 바라본다
# 방향 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽


# 현재 위치에서 왼쪽으로 3번 돌아보기: 갈 수 있는 칸이 있는지 체크
# 갈 수 있는 칸이 있는 경우: [direction, True, xPos, yPos]를 return
# 전진할 수 없는 경우: [direction, False]를 return
def moveLeft(direction, xPos, yPos):
    returnValue = []
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    returnValue.append(direction)
    
    if direction == 0:  #  북쪽
        if yPos != 0 and gameMap[xPos][yPos-1] == 0:
            returnValue.append(True)
            yPos -= 1
        else:
            returnValue.append(False)
            return returnValue
    elif direction == 1:    # 동쪽
        if xPos != M-1 and gameMap[xPos+1][yPos] == 0:
            returnValue.append(True)
            xPos += 1
        else:
            returnValue.append(False)
            return returnValue
    elif direction == 2:    # 남쪽
        if yPos != N-1 and gameMap[xPos][yPos+1] == 0:
            returnValue.append(True)
            yPos += 1
        else:
            returnValue.append(False)
            return returnValue
    else:   # 서쪽
        if xPos != 0 and gameMap[xPos-1][yPos] == 0:
            returnValue.append(True)
            xPos -= 1
        else:
            returnValue.append(False)
            return returnValue
    
    returnValue.append(xPos)
    returnValue.append(yPos)
    return returnValue

N, M = map(int, input().split())    # N: 세로 크기, M: 가로 크기
playerXPos, playerYPos, playerDirect = map(int, input().split())
gameMap = []    # 방문하지 않은 육지: 0, 바다: 1, 방문한 육지: 2
for _ in range(N):
    gameMap.append(list(map(int, input().split())))
gameMap[playerXPos][playerYPos] = 2
answer = 0

while True:
    visited = False
    # 3번 돌았는데 모두 가본 칸 or 바다로 되어 있는 경우: 뒤로 한 칸
    # 뒤로 가야되는데 뒤가 바다면 stop

    for _ in range(3):
        returnValue = moveLeft(playerDirect, playerXPos, playerYPos)
        playerDirect = returnValue[0]
        if returnValue[1] == True:
            # 현재 바라보고 있는 방향으로 전진 가능
            playerXPos = returnValue[2]
            playerYPos = returnValue[3]
            gameMap[playerXPos][playerYPos] = 2
            visited = True
            answer += 1
            break
    
    if visited == False:
        if playerDirect == 0 and playerYPos != N-1 and gameMap[playerXPos][playerYPos+1] != 1:    # 북쪽
            playerYPos += 1
        elif playerDirect == 1 and playerXPos != 0 and gameMap[playerXPos-1][playerYPos] != 1:  # 동쪽
            playerXPos -= 1
        elif playerDirect == 2 and playerYPos != 0 and gameMap[playerXPos][playerYPos+1] != 1:  # 남쪽
            playerYPos += 1
        elif playerDirect == 3 and playerXPos != M-1 and gameMap[playerXPos+1][playerYPos] != 1: # 서쪽
            playerXPos += 1
        else:
            print(answer)
            break
        answer += 1 # 뒤로 한 칸 이동

