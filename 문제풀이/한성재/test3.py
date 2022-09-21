import collections
import enum


arr = [
       ["한성재", "이정훈", "안한승", "신영준", "최강"],
    ["안유나", "강재현", "김도운", "한정민", "정일훈", "장예진", "최강"],
       ["한성재", "강재현", "안유나", "신영준", "정일훈", "정민규"],
       ["김민철", "김도운", "이정훈", "신영준", "장예진", "정민규"],
       ["김민철", "강재현", "안유나", "한정민", "장예진", "최강"]
       ["안유나", "강재현", "김도운", "신영준", "정민규"],
       ["한성재", "강재현", "이정훈", "한정민", "김은재"],
       ]

dict = collections.defaultdict(int)
for elem in arr:
    for name in elem:
        dict[name] += 1

print(sorted(dict.items(), key=lambda x: x[1]))
