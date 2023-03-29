import re

express_1 = re.compile('(100+1+|01)+')

case = int(input())
for i in range(case):
    sentance = input().rstrip()
    result = express_1.fullmatch(sentance)
    if result:
        print('YES')
    else :
        print('NO')

        # 10011001