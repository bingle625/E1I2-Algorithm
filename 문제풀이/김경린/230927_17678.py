from collections import deque

def time_to_char(t, m):
    return  (str(t) if t > 9 else ("0"+str(t))) + ":" + (str(m) if m > 9 else ("0" + str(m)))

def is_bigger(time, cur_t, cur_m):
    if time > time_to_char(cur_t, cur_m):
        return True
    else:
        return False
    

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    timetable = deque(timetable)
    cur_time = 9*60
    fin_time = 9*60+(n-1)*t
    

    
    while n > 0 and len(timetable) > 0:
        cur_t = cur_time//60
        cur_m = cur_time%60
  
        if is_bigger(timetable[0], cur_t, cur_m):
            cur_time += t
            n -= 1
            continue
        else:
            copy_m = m
            while copy_m>0 and len(timetable)>0 and not is_bigger(timetable[0], cur_t, cur_m):
                last = timetable.popleft()
                copy_m -= 1

            # 마지막 셔틀
            if n == 1 and copy_m == 0:
                fin_time = int(last[0:2])*60+int(last[-2:]) - 1
                print(fin_time)
        
                           
        cur_time += t  
        n -= 1
  
    answer = time_to_char(fin_time//60, fin_time%60)
        
    return answer