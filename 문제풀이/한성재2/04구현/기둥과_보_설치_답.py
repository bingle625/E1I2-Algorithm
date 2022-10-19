

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥일 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False # 아니라면 False 반환
        elif stuff == 1: # 보일 경우
            # 한쪽 끝 부분이 '기둥 위' 혹은 '양족 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1]in answer and [x+1,y,1] in answer):
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
            answer.remove([x,y,stuff]) #일단 삭제를 해본뒤에
            if not possible(answer):
                answer.append([x,y,stuff]) # 안되면 다시 설치
        if operate == 1:
            answer.append([x,y,stuff]) #일단 설치를 해본 뒤에
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)
    
print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))