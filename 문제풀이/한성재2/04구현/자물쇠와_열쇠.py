key1 = [[0,0,0],
        [1,0,0],
        [0,1,1]]

lock1 = [[1,1,1],
         [1,1,0],
         [1,0,1]]

def solution(key, lock):
    for i in range(4):
        print(key)
        for i in range(len(key)):
            for k in range(len(key)):
                print(key[i][k],end="")
            print("")
        for i in range(len(key)):
            for k in range(len(key)-1,-1,-1):
                print(i,k)
                key[i][k],key[k][i] = key[k][i],key[i][k]
    answer = True
    return answer

solution(key1,lock1)