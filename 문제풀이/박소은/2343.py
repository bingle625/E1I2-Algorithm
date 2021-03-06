# N 개의 강의, M 개의 블루레이

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

# length: 최소한 max(lectures)이상, sum(lectures)이하
left, right = max(lectures), sum(lectures)
lengths = [0]

while left <= right:
    mid = left + (right - left) // 2    # lengths의 최대 길이(limit)

    i = 0
    for lecture in lectures:
        if lengths[i] + lecture <= mid:
            lengths[i] += lecture
        else:
            lengths.append(lecture)
            i += 1
    
    if len(lengths) > M:
        # cd 크기를 늘려야 됨
        left = mid + 1
    else:
        right = mid - 1
    lengths = [0]

print(left)