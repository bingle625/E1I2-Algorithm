
num = int(input())

origin = []
tmpList = []
ans = []
for i in range(num):
    tmp = int(input())
    origin.append(tmp)

i = 0
for j in range(1, num+1):
    tmpList.append(j)
    print('+')
    if origin[i] == j:
        tmp = tmpList.pop()
        ans.append(tmp)
        print('-')
        i += 1
        while len(tmpList):
            top = tmpList.pop()
            if top == origin[i]:
                ans.append(top)
                print('-')
                i += 1
            else:
                tmpList.append(top)
                break
