
from collections import defaultdict, deque


class TrieNode():
    
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word_list):
        node = self.root
        for word in word_list:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.word = True
    

def preorder(node,cnt):
    cnt += 1
    sorted_child = sorted(node.children)
    for child in sorted_child:
        for i in range(cnt-1):
            print('--',end='')
        print(child)
        preorder(node.children[child],cnt)

ant_num = int(input())
trie = Trie()
for i in range(ant_num):
    word_list = deque(input().split())
    word_list.popleft()
    trie.insert(word_list)

preorder(trie.root,0)






