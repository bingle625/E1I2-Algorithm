
    

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_pos, p_pos = n-1, n-1
    if sum(deliveries) == 0 and sum(pickups) == 0:
        return 0
    while d_pos > -1 or p_pos > -1:
        move = max(d_pos+1, p_pos+1)
        avail_d, avail_p = cap, cap
        
        while avail_d > 0 and d_pos > -1:
            if deliveries[d_pos] > avail_d:
                deliveries[d_pos] -= avail_d
                avail_d = 0
            else:
                avail_d -= deliveries[d_pos]
                deliveries[d_pos] = 0
                while deliveries[d_pos] == 0 and d_pos > -1:
                    d_pos -= 1
                
        while avail_p > 0 and p_pos > -1:
            if pickups[p_pos] > avail_p:
                pickups[p_pos] -= avail_p
                avail_p = 0
            else:
                avail_p -= pickups[p_pos]
                pickups[p_pos] = 0
                while pickups[p_pos] == 0 and p_pos > -1:
                    p_pos -= 1
    
        answer += 2*move
    
    return answer