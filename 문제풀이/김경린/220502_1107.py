import sys


target = int(input())

brokenNum = int(input())
broken = []
if brokenNum:
    broken = list(input().split())


manual = abs(target - 100)
time = sys.maxsize

for i in range(1000000):
    ok = 1
    for j in str(i):
        if j in broken:
            ok = 0
            break
    if ok==1:
        time = min(time, len(str(i)) + abs(target - i))

print(min(time,manual))
    






# 오류 코드
# target = list(target)
# bigger = [ 9 for _ in range(len(target))] # 해당 숫자가 타겟보다 커지면 무조건 뒷 자리숫자들은 작은게 유리
# smaller = [ 0 for _ in range(len(target))]
# same = 1
# for i in range(len(target)):
#     src = target[i]
#     if same:
#         if int(src) in broken:
#             for j in range(1,10):

#                 numMinus = int(target[i]) - j
#                 numPlus = int(target[i]) + j
                
#                 if numMinus < 0:
#                     numMinus = ''
                    
        
#                 if bigger[i] == 9 and numPlus not in broken:
#                     bigger[i] = str(numPlus)
    
#                 if smaller[i] == 0 and numMinus not in broken:
#                     smaller[i] = str(numMinus)
                
#                 if bigger[i] != 9 and smaller[i] != 0:
#                     break
                    
#             same = 0
#         else:
#             bigger[i] = target[i]
#             smaller[i] = target[i]
#     else:

#         for j in range(0,10):
#             if j not in broken:
#                 bigger[i] = str(j)
#                 break

#         for j in range(9,-1,-1):
#             if j not in broken:
#                 smaller[i] = str(j)
#                 break
    
        
                


# bigNum = ''.join(str(x) for x in bigger)
# smNum = ''.join(str(x) for x in smaller)
# bigTime = len(bigNum) + abs(int(bigNum)-int(origin))
# smallTime = len(smNum) + abs(int(smNum)-int(origin))
# print(min(bigTime,smallTime,manual))