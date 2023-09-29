# 프로그래머스 81303
class Node():
    def __init__(self, idx, last_node=None, next_node=None):
        self.idx = idx
        self.last_node = last_node
        self.next_node = next_node

    
    
    

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    for i in range(n):
        node = Node(i)
        if i!= 0:
            last_node.next_node = node
            node.last_node = last_node
        if i == k:
            target = node
        last_node = node
        
    deleted = []
    start_idx = 0
    final_idx = n-1
    for c in cmd:
        if c[0] == 'C':
            deleted.append(target)
            if target.idx == start_idx:
                target.next_node.last_node = None
                start_idx = target.next_node.idx
                target = target.next_node
            elif target.idx == final_idx:
                target.last_node.next_node = None
                final_idx = target.last_node.idx
                target = target.last_node
            else:
                target.last_node.next_node = target.next_node
                target.next_node.last_node = target.last_node 
                target = target.next_node
        elif c[0] == 'Z':
            if len(deleted):
                node = deleted.pop()
                if node.idx < start_idx:
                    start_idx = node.idx
                    node.next_node.last_node = node
                elif node.idx > final_idx:
                    final_idx = node.idx
                    node.last_node.next_node = node
                else:
                    node.last_node.next_node = node
                    node.next_node.last_node = node
        elif c[0] == 'U':
            tmp = c.split(' ')
            for i in range(int(tmp[1])):
                if target.idx != start_idx:
                    target = target.last_node
        elif c[0] == 'D':
            tmp = c.split(' ')
            for i in range(int(tmp[1])):
                if target.idx != final_idx:
                    target = target.next_node
        
    for node in deleted:
        answer[node.idx] = 'X'
        
    
    return ''.join(answer)