# from collections import defaultdict
# import copy

# def compare_after(current, after):
#     sum_char = ''
#     if current == after[:len(current)]:
#         return len(current)
#     else:
#         cnt = 0
#         for char in current:
#             sum_char += char
#             cnt += 1
#             if sum_char != after[:cnt]:
#                 return len(sum_char)
# def compare_before(current, before):
#     sum_char = ''
#     if before == current[:len(before)]:
#         return len(before) + 1
#     else:
#         cnt = 0
#         for char in current:
#             sum_char += char
#             cnt += 1
#             if sum_char != before[:cnt]:
#                 return len(sum_char)

# def solution(words):
#     answer = 0
#     words.sort()
#     words_dict = defaultdict(int)
    
#     answer += compare_after(words[0], words[1])
    
#     for i in range(1, len(words)-1):
#         answer += max(compare_before(words[i], words[i-1]), compare_after(words[i], words[i+1]))
#     answer += compare_after(words[-1], words[-2])
        
#     return answer


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.cnt = 0
        

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.cnt += 1
        
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        char_length = 0
        for char in string:
            char_length += 1
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                if curr_node.cnt == 1:
                    return char_length
        return len(string)

def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)
    
    return answer