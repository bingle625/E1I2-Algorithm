def solution(n, stations, w):
    answer = 0
    end = 0
    cnt = 0
    for station in stations:
        val = station-w-1-end
        if val > 0:
            d = val % (2*w+1)
            cnt += val // (2*w+1) + (1 if d > 0 else 0)
        end = station + w
    
    val = n - end
    if val > 0:
        d = val % (2*w+1)
        cnt += val // (2*w+1) + (1 if d > 0 else 0)

    return cnt