lines = input()
split_line = []
num = []    # 숫자를 잠시 저장할 리스트
cal_line = []   # 계산할 문자열을 저장

for line in lines:
    if (line >= '0') and (line <= '9'):
        num.append(line)
    else:
        split_line.append(int("".join(num)))
        num = []
        split_line.append(line)
split_line.append(int(''.join(num)))


for i in range(len(split_line)):
    cal_line.append(split_line[i])
    if (split_line[i] == '-'):
        cal_line.append('(')
    
