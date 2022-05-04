# 필요한 나무 M미터, 절단기 높이 지정 H미터
import bisect

def max_height(M, trees):
    trees.sort(reverse=True)    # [20, 17, 15, 19]
    M_list = []     # 나무 별 얻을 수 있는 개수 합
    prev, sum = trees[0], 0

    for idx, tree in enumerate(trees):
        sum += (prev - tree) * idx
        M_list.append(sum)
        prev = tree
    
    index = bisect.bisect_left(M_list, M)
    if index < len(trees):
        H = trees[index] + (M_list[index] - M) // index
    else:   # M > M_list[len(M_list)-1] 일 때 (index==len(M_list))
        if (M - M_list[index-1]) % index == 0:
            H = trees[index-1] - (M - M_list[index-1]) // index
        else:
            H = trees[index-1] - (M - M_list[index-1]) // index - 1
            if H < 0:   # 나무를 모두 베어야 할 때
                H = 0
    
    return H

    # [0, 3, 3 + 2*2, 3 + 2*2 + 5*3]  # M_list
    # [20, 17, 15, 10]    # trees
    # [0 , 3 ,  7, 22]    # 얻을 수 있는 개수(M_list)
    # M=26 22+4 -> 9
    # M=30 22+8 -> 8

treeNum, M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))

print(max_height(M, trees))