from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    parking = defaultdict(list)
    for record in records:
        time, num, isIn = record.split(" ")
        hour, minute = map(int, time.split(":"))
        parking[num].append(hour*60+minute)
    sorted_key = sorted(parking.keys())
    for key in sorted_key:
        if len(parking[key])%2 == 1:
            parking[key].append(23*60+59)
        parking_time = 0
        for i in range(len(parking[key])//2):
            parking_time += parking[key][i*2+1] - parking[key][2*i]
        if parking_time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((parking_time-fees[0])/fees[2])*fees[3])
                       
            
    return answer