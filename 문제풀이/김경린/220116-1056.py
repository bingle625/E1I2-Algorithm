def n_set(list_a: list, n: int):
    list_a.sort()
    for i in range(len(list_a)):
        if list_a[i] == n:
            return 0
        elif list_a[i] > n:
            if i != 0:
                range_l = n - list_a[i-1]
                range_r = list_a[i] - n
                range_a = (range_l)*(range_r)-1
                return range_a
            else:
                range_l = n
                range_r = list_a[i]-n
                range_a = (range_l)*(range_r)-1
                return range_a


num = int(input())
list_a = list(map(int, input().split()))
n = int(input())
print(n_set(list_a, n))
