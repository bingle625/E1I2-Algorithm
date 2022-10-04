# p.316 06. 무지의 먹방 라이브
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42891

food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    foodCount = len(food_times)
    minusCount = 0  # 전체 배열에서 minusCount만큼 빼기
    
    while k > foodCount:
        minusCount += 1 # 전체 배열에서 1개씩 빼기
        k -= foodCount  
        foodCount -= food_times.count(minusCount)   # 다 먹은 음식 처리해서 foodCount에서 빼기

    # k=2, [2,0,4], foodCount=2인 상태로 끝남.
    while k >= 0:
        for idx, food_time in enumerate(food_times):
            # print("idx: ", idx, "food_time: ", food_time)
            if food_time <= minusCount:
                # print("pass~")
                continue
            if k == 0:
                return idx + 1
            k -= 1
        minusCount += 1

# 정답: 1
print(solution(food_times, k))