# 런타임 에러

from typing import List

def sorting(num: int) -> List[int]:
    words = []

    for i in range(num):
        words.append(input())
    
    for word in words:
        if(words.count(word) > 1):
            words.remove(word)
    
    sorted(words, key = len)

    return words

print(sorting(int(input())))