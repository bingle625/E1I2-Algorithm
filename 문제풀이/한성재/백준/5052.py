# 5052번 전화번호 목록

# 1. 이미 존재하는 접두사가 또 추가 되었을 때
# 2. 존재하지 않는 접두사가 추가되었을 때


import collections
import sys


class trieNode:
    def __init__(self):
        self.end = False
        self.children = collections.defaultdict(trieNode)


class solution:

    def __init__(self):
        self.root = trieNode()

    def __iter__(self):
        return self

    def __next__(self):
        self.root = None
        self.root = trieNode()

    def trieTraverse(self, phoneNum: list):
        node = self.root

        for number in phoneNum:
            node = node.children[number]
            if node.end:
                return False
        if node.children:
            return False
        node.end = True
        return True


testCase = int(input())

for _ in range(testCase):
    N = int(input())
    s = solution()

    answer = True
    for case in range(N):
        user_input = sys.stdin.readline().rstrip()

        if s.trieTraverse(list(map(int, user_input))) is not True:
            answer = False

    if answer:
        print("YES")
    else:
        print("NO")

    s = None
