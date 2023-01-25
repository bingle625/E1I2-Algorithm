from collections import defaultdict 

def solution(enroll, referral, seller, amount):
    answer = []
    profit_dict = defaultdict(int)
    parent_dict = defaultdict(str)
    for i in range(len(enroll)):
        if referral[i] != "-":
            parent_dict[enroll[i]] = referral[i]
    for i in range(len(seller)):
        sell = amount[i]*100
        profit_dict[seller[i]] += sell*0.9
        child = seller[i]
        sell *= 0.1
        while parent_dict[child] != '' and int(sell*0.1) >= 1:
            child = parent_dict[child]
            profit_dict[child] += (sell - int(sell*0.1))
            sell = int(sell*0.1)
        profit_dict[parent_dict[child]] += sell
            
    
    for name in enroll:
        answer.append(profit_dict[name])
        
    return answer