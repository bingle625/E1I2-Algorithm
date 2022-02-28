# 0,1,2,3,4,5,6,7,8,6, 이 한세트
# 입력으로 9가 들어오면 6으로 치환

import collections


def print_set(number: str) -> None:
    number_map = collections.Counter(list(number))
    max = 0

    number_map['6'] = number_map['6'] + number_map['9']
    number_map['9'] = 0
    number_map['6'] = number_map['6'] // 2 + number_map['6'] % 2

    for v in number_map.values():
        if v > max:
            max = v
    print(max)


num = input()

print_set(num)
