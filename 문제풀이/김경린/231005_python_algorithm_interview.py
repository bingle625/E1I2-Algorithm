# from collections import defaultdict



# ## 이진 탐색
# from collections import deque

# def solution():
#     nums = [4, 5, 6, 7, 0, 1, 2]
#     nums = deque(nums)
#     target = 1
    
#     turn_cnt = 0

#     while nums[-1] <= nums[0]:
#         tmp = nums.popleft()
#         nums.append(tmp)
#         turn_cnt += 1
    
#     start = 0
#     end = len(nums) - 1

#     while start < end:
#         idx = (start + end)//2
#         if nums[idx] < target:
#             start = idx
#         elif nums[idx] > target:
#             end = idx
#         else:
#             return idx + turn_cnt

# print(solution())


## 슬라이딩 윈도우

## 슬라이딩 윈도우는 고정된 사이즈, 정렬되지 않은 배열에서 사용

# from collections import deque

# def solution():
#     nums = [1,3,-1,-3,5,3,6,7]
#     answer = []
#     tmp = deque()
#     k = 3
#     length = 0
#     max_num = nums[0]
#     out = 
#     for i in range(len(nums)):
#         length += 1
#         tmp.append(nums[i])
#         if length == k:
#             if nums[i] > max_num:
#                 max_num = nums[i]
#             elif out == max_num:
#                 max_num = max(tmp)
#             answer.append(max_num)
#             length -= 1
#             out = tmp.popleft()
    
#     print(answer)

# solution()


### 트라이

# from sys import stdin
# class Node():
#     def __init__(self, char=None):
#         self.char = char
#         self.children = {}
#         self.is_end = False
    
# class Trie():
#     def __init__(self):
#         self.head = Node()
    
#     def insert(self, string):
#         node = self.head

#         for s in string:
#             if s not in node.children:
#                 node.children[s] = Node(s)
#             node = node.children[s]

#         node.is_end = True
    
#     def search(self, string):
#         node = self.head
#         for s in string:
#             if s not in node.children:
#                 return False
#             node = node.children[s]
#         if node.is_end:
#             return True
#         else:
#             return False

# n, m = map(int, stdin.readline().rstrip().split(' '))
# trie = Trie()

# for _ in range(n):
#     string = stdin.readline().rstrip()
#     trie.insert(string)

# cnt = 0
# for _ in range(m):
#     string = input()
#     if trie.search(string):
#         cnt += 1

# print(cnt)

### 투포인터
def minWindow(s: str, t: str) -> str:
        from collections import defaultdict

        start_idx = 0
        fin_idx = len(s)-1
        min_start = 0
        min_fin = len(s) - 1
        nums = {}
        t_nums = {}
        for char in t:
            t_nums[char] = 1
        
        for idx, val in enumerate(s):
            if val not in t_nums.keys():
                continue
            if val in nums:
                nums[val] += 1
            else:
                nums[val] = 1
            
            if nums.keys() == t_nums.keys():
                start = start_idx
                while s[start] not in t_nums or nums[s[start]] > 1:
                    if s[start] in t_nums:
                        nums[s[start]] -= 1
                    start += 1
                start_idx = start
                fin_idx = idx

                if (min_fin - min_start) > fin_idx-start_idx:
                    min_start = start_idx
                    min_fin = fin_idx 

        return s[min_start:min_fin+1]

print(minWindow("ADOBECODEBANC", "ABC"))
