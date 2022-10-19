def solution(n, build_frame):
    answer = []
    cols = []
    bars = []
    directions = [(0,1), (1,0)]
    
    for cmd in build_frame:
        # 1. 삭제인가 설치인가.
        #삭제인 경우
        if cmd[3] == 0:
            if cmd[:3] in answer:
                
                #기둥인 경우
                if cmd[2] == 0:
                    success = True
                    
                    #다른 기둥의 받침인가
                    if [cmd[0]+directions[0][0], cmd[1]+directions[0][1], 0] in answer:
                        success = False
                    # 다른 보의 받침인가, 그럻다면, 그 보가 만족그 보의 반대쪽에 다른 기둥이 없나
                    if [cmd[0]+directions[0][0], cmd[1]+directions[0][1], 1] in answer:
                        if [cmd[0]+directions[0][0]+1,cmd[1], 0] not in answer:
                             success = False
                    if [cmd[0]-1, cmd[1]+directions[0][1], 1] in answer:
                        if [cmd[0]-1,cmd[1], 0] not in answer:
                             success = False
                    if success == True:
                        cols.remove((cmd[0],cmd[1]))
                        cols.remove((cmd[0]+directions[0][0],cmd[1]+directions[0][1]))
                        answer.remove(cmd[:3])
                #보인 경우
                else:
                    success = True
                    #다른 기둥의 받침인가
                    if [cmd[0],cmd[1],0] in answer:
                        success = False
                    if [cmd[0]+directions[1][0], cmd[1]+directions[1][1], 0] in answer:
                        success = False
                        
                    #이웃한 보가 있는가, 있다면 그 보에 다른 기둥이 없나
                    if [cmd[0]-1,cmd[1],1] in answer:
                        if [cmd[0]-1,cmd[1]-1,0] not in answer:
                            success= False
                    
                    if [cmd[0]+1,cmd[1],1] in answer:
                        if [cmd[0]+2,cmd[1]-1,0] not in answer:
                            success= False
                    
                    if success:
                        bars.remove((cmd[0],cmd[1]))
                        bars.remove((cmd[0]+directions[1][0],cmd[1]+directions[1][1]))
                        answer.remove(cmd[:3])

            #설치인 경우
        else:
            #기둥인 경우
            if cmd[2] == 0:
                success = False
                if cmd[1] == 0:
                    success= True
                if (cmd[0],cmd[1]) in bars:
                    success= True
                if (cmd[0],cmd[1]) in cols and [cmd[0],cmd[1],0] not in answer:
                    success= True
                
                if cmd[1]>n or cmd[1] + directions[0][1] > n:
                    success = False
                
                if success == True:
                    cols.append((cmd[0],cmd[1]))
                    cols.append((cmd[0]+directions[0][0],cmd[1]+directions[0][1]))
                    answer.append([cmd[0],cmd[1],0])
            # 보인 경우
            else:
                success = False
                if (cmd[0],cmd[1]) in cols or (cmd[0]+directions[1][0],cmd[1]+directions[1][1]) in cols:
                    success= True
                if (cmd[0],cmd[1]) in bars and (cmd[0]+directions[1][0],cmd[1]+directions[1][1]) in bars:
                    success= True

                if cmd[0] > n or cmd[0] + directions[1][0] > n:
                    success = False
                    
                if success == True:
                    bars.append((cmd[0],cmd[1]))
                    bars.append((cmd[0]+directions[1][0],cmd[1]+directions[1][1]))
                    answer.append([cmd[0],cmd[1],1])
    
    answer.sort(key=lambda x: x[1])
    answer.sort(key=lambda x: x[0])
    
    return answer






print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))