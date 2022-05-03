# 그룹 애너그램 / 풀이가 섞였음. 다시
import collections


def is_Ana(str1, str2):
    if str1.sort() == str2.sort():
        return True


in_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = collections.defaultdict(list)

for str in in_str:
    res[''.join(sorted(str))].append(str)

print(list(res.values()))
