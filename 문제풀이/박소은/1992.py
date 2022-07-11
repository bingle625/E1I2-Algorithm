import sys

def compress(treeList, size) -> str:
    char = treeList[0][0]
    for i in treeList:
        if (i != "0"*size and i != "1"*size) or char != i[0]:
            # 4등분해서 각각 리스트 따로 만들기
            first = []
            second = []
            third = []
            fourth = []
            string = []
            for j in range(size):
                if j < size/2:
                    first.append(treeList[j][:size//2])
                    second.append(treeList[j][size//2:])
                else:
                    third.append(treeList[j][:size//2])
                    fourth.append(treeList[j][size//2:])
            
            # 다시 compress 호출
            string.append(compress(first, size//2))
            string.append(compress(second, size//2))
            string.append(compress(third, size//2))
            string.append(compress(fourth, size//2))
            return "(" + ''.join(string) + ")"
    if treeList[0][0] == "0":
        return "0"
    else:
        return "1"

inputNum = int(input())
lines = []
for _ in range(inputNum):
    lines.append(sys.stdin.readline().strip())
print(compress(lines, inputNum))
