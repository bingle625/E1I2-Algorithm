
num = int(input())

origin = []
tmpList = []
ans = []
sign = []
for i in range(num):
    tmp = int(input())
    origin.append(tmp)

i = 0
for j in range(1, num+1):
    tmpList.append(j)
    sign.append('+')
    if origin[i] == j:
        tmp = tmpList.pop()
        ans.append(tmp)
        sign.append('-')
        i += 1
        while len(tmpList):
            top = tmpList.pop()
            if top == origin[i]:
                ans.append(top)
                sign.append('-')
                i += 1
            else:
                tmpList.append(top)
                break

if len(ans) != len(origin):
    print("NO")
else:
    for i in sign:
        print(i)
