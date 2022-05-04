
num = int(input())

num_list = list(map(int,input().split()))

#값만 복사하기
tmp = list(set(num_list))
tmp.sort()



for i in range(len(num_list)):
    start = 0
    end = len(tmp)   
    while True:
        idx = (start+end)//2
        if num_list[i]>tmp[idx]:
            start = idx+1
        elif num_list[i]<tmp[idx]:
            end = idx-1
        else:
            print(idx,end=' ')
            break
