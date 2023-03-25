from collections import defaultdict
def get_finish_date(start_date, term):
    y, m, d = map(int, start_date.split('.'))
    m += term
    if m>12:
        if m%12==0:
            y += m//12 - 1
            m = 12
        else:
            y += m//12
            m = m%12
   

    y = str(y)
    if m < 10:
        m = '0'+ str(m)
    else:
        m = str(m)
    if d < 10:
        d = '0' + str(d)
    else:
        d = str(d)
    return y+'.'+ m +'.'+ d
     

def solution(today, terms, privacies):
    answer = []
    
    terms_dict = defaultdict(int)
    for term in terms:
        type, period = term.split(' ')
        terms_dict[type] = int(period)
    
    for idx in range(len(privacies)):
        start_date, term = privacies[idx].split(' ')
        term = terms_dict[term]
        finish_date = get_finish_date(start_date, term)
        if finish_date <= today:
            answer.append(idx+1)

        
    return answer
