import sys


class Node():
    def __init__(self, num=None):
        self.num = num
        self.next = []
        
    

start = Node()
last_node = start
special_nodes = []
for i in range(1, 21):
    last_node.next.append(Node(num=2*i))
    last_node = last_node.next[0]
    if 2*i%10==0:
        special_nodes.append(last_node)

fin_node = last_node

for s in special_nodes:
    if s.num == 10:
        s.next.append(Node(13))
        node = s.next[1]
        node.next.append(Node(16))
        node = node.next[0]
        node.next.append(Node(19))
        node = node.next[0]
        node.next.append(Node(25))
        node_25 = node.next[0]
    elif s.num == 20:
        s.next.append(Node(22))
        node = s.next[1]
        node.next.append(Node(24))
        node = node.next[0]
        node.next.append(node_25)
    elif s.num == 30:
        s.next.append(Node(28))
        node = s.next[1]
        node.next.append(Node(27))
        node = node.next[0]
        node.next.append(Node(26))
        node = node.next[0]
        node.next.append(node_25)

        node = node_25
        node.next.append(Node(30))
        node = node.next[0]
        node.next.append(Node(35))
        node = node.next[0]
        node.next.append(fin_node)
        node = node.next[0]
        node.next.append(Node(-1))
        fin_node = fin_node.next

horses = [start, start, start, start]

counts = list(map(int, input().split(' ')))
max_num = -sys.maxsize

def all_horses_goal(horses):
    if (horses[0].num == -1  and horses[1].num == -1 and horses[2].num == -1 and horses[3].num == -1):
        return True
    else:
        return False

def go(horse, cnt, val):
    for i in range(cnt):
        if horse.num == -1:
            return horse, val
        elif i == 0 and len(horse.next) > 1:
            horse = horse.next[1]
        else:
            horse = horse.next[0]
    # print(horse)
    val += horse.num
    return horse, val


def dfs(depth, horses, val):
    # print(val)
    global max_num
    # val_origin = val
    if depth >= 10:
        max_num = max(max_num, val)
        # for i in range(4):
        #     print(horses[i].num, end=' ')
        # print(' ', val)
        return
    for i in range(4):
        if horses[i].num != -1:
            last_horse = horses[i]
            new_horse, new_val = go(horses[i], counts[depth], val)
            if new_horse.num != -1 and new_horse in horses:
                continue
            horses[i] = new_horse
            dfs(depth+1, horses, new_val)
            horses[i] = last_horse

    if all_horses_goal(horses):
        max_num = max(max_num, val)
        return
    


dfs(0, horses, 0)


print(max_num)