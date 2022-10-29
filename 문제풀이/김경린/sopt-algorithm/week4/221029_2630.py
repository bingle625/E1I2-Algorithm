from sys import stdin
def is_same(arr):
    standard = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != standard:
                return False
        
    return True


size = int(stdin.readline())
arr = [0 for _ in range(size)]
for i in range(size):
    arr[i] = list(map(int, stdin.readline().strip().split()))

b = 0
w = 0
def cnt_paper(arr):
    global b,w
    if len(arr) == 2:
        for i in range(2):
            for j in range(2):
                if arr[i][j] == 0:
                    w += 1
                else:
                    b += 1
        return 0
    arr1 = []
    for i in range(len(arr)//2):
        arr1.append(arr[i][:len(arr[0])//2])
    if is_same(arr1):
        if arr1[0][0]==0:
            w +=1
        else:
            b += 1
    else:
        cnt_paper(arr1)
    
    arr2 = []
    for i in range(len(arr)//2):
        arr2.append(arr[i][len(arr[0])//2:])
    if is_same(arr2):
        if arr2[0][0]==0:
            w +=1
        else:
            b += 1
    else:
        cnt_paper(arr2)
    
    arr3 = []
    for i in range(len(arr)//2,len(arr)):
        arr3.append(arr[i][:len(arr[0])//2])
    if is_same(arr3):
        if arr3[0][0]==0:
            w +=1
        else:
            b += 1
    else:
        cnt_paper(arr3)
    
    arr4 = []
    for i in range(len(arr)//2, len(arr)):
        arr4.append(arr[i][len(arr[0])//2:])
    if is_same(arr4):
        if arr4[0][0]==0:
            w +=1
        else:
            b += 1
    else:
        cnt_paper(arr4)

if is_same(arr):
    if arr[0][0] == 0:
        w += 1
    else:
        b += 1
else:
    cnt_paper(arr)
print(w)
print(b)