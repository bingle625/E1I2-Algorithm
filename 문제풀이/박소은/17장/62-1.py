# 풀이 1: 정렬을 이용한 비교

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)