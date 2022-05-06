# N 개의 강의, M 개의 블루레이

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

# length: 최소한 max(lectures)보다는 크고 sum(lectures)보다는 작아야 함
left, right = max(lectures), sum(lectures)
lengths = [0]

while left <= right:
    mid = left + (right - left) // 2

    i = 0
    for lecture in lectures:
        if lengths[i] + lecture <= mid:
            lengths[i] += lecture
        else:
            lengths.append(lecture)
            i += 1
    
    if len(lengths) == M:
        print(max(lengths))
        break
    elif len(lengths) > M:
        # cd 크기를 늘려야 됨
        left = mid + 1
    else:
        right = mid - 1
    lengths = [0]