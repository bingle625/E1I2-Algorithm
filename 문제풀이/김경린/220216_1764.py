
N,M =input().split()

N = int(N)
M = int(M)

non_heard = []
non_seen = []

for i in range(N):
    tmp = input()
    non_heard.append(tmp)


for i in range(M):
    tmp = input()
    non_seen.append(tmp)

not_known = list(set(non_seen)&set(non_heard))
not_known.sort()
print(len(not_known))
for name in not_known:
    print(name)
        

