s, l = map(int, input().split(' '))

def find_sum(s, l):
    for i in range(l, 101):
        sum_i = (i-1)*i/2
        st = (s - sum_i)
        if st%i == 0 and st >= 0:
            start = int(st//i)
            ans = []
            for j in range(i):
                ans.append(start+j)
            return ans
    return [-1]

ans = find_sum(s,l)
print(' '.join(str(_) for _ in  ans))

