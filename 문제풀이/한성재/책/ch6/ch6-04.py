# 04번 책 답안
import collections
import re

paragraph = "Bob, hit a ball, the hit Ball flew far after it was hit."
banned = ["hit"]
paragraph2 = ["h", "e", " ", "l", "o"]
print(re.sub(r'[^\w]', ' ', paragraph).lower())

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
         if word not in banned]

# print(words)
counts = collections.Counter(words)

print(counts.most_common(1)[0][0])
