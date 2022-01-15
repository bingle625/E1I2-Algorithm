# 2947 나무 조각

num_list = list(map(int, input().split()))

sum = 1
while(sum):
    sum = 0
    for i in range(len(num_list)-1):
        if(num_list[i] > num_list[i+1]):
            sum += 1
            temp = num_list[i]
            num_list[i] = num_list[i+1]
            num_list[i+1] = temp

            print(' '.join(str(_) for _ in num_list))
