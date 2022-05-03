import collections



def first_max(queue, idx):
    while True:
        max_queue = max(queue)
        tmp = queue.popleft()
        if len(queue) == 0:
            idx = -1
            break
        if tmp == max_queue:
            idx -= 1
            break
        if tmp != max_queue:
            idx -= 1
            queue.append(tmp)
            if idx < 0:
                idx = len(queue)-1

    return queue, idx


case = int(input())
for i in range(case):
    doc_num, idx = map(int, input().split())
    docs = map(int, input().split())
    queue = collections.deque()
    for doc in docs:
        queue.append(doc)

    cnt = 0
    while True:
        origin_idx = idx
        queue, idx = first_max(queue, idx)
        cnt += 1
        if idx == -1:
            print(cnt)
            break


#힙큐

