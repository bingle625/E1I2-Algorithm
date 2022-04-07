
cargo = []

num,capacity = map(int,input().split())

for i in range(num):
    w,v = map(int,input().split())
    cargo.append((w,v))

pack = []

for i in range(len(cargo)+1):
    pack.append([])
    for c in range(capacity+1):
        if i==0 or c==0:
            pack[i].append(0)
        
        elif cargo[i-1][0]<= c:
            pack[i].append(max(pack[i-1][c],cargo[i-1][1]+pack[i-1][c-cargo[i-1][0]]))
        else:
            pack[i].append(pack[i-1][c])

print(pack[-1][-1])
