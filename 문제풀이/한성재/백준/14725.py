# 14725. 개미굴

import collections
import sys


class TrieNode:
    def __init__(self) -> None:
        self.end = False
        self.child = collections.defaultdict(TrieNode)
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, words: list):
        node = self.root
        for word in words:
            node = node.child[word]
    
    def printResult(self, node: TrieNode,stairs=""):
        now_stairs =stairs + "--"
        
        for children in sorted(node.child.keys()):
            print(stairs+children)
            self.printResult(node.child[children],now_stairs)

road_case = int(input())
test = Trie()

for _ in range(road_case):
    road = list(sys.stdin.readline().strip().split())
    test.insert(road[1:])

test.printResult(test.root)