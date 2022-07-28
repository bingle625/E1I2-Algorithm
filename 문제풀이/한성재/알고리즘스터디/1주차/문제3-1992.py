from sys import stdin


number = int(input())
mat = []

for i in range(number):
    mat.append(list(stdin.readline().rstrip()))


def getArc(leftStart, upStart, amount):
    if amount == 1:
        return str(mat[upStart][leftStart])

    standard = mat[upStart][leftStart]
    for i in range(leftStart, leftStart+amount):
        for k in range(upStart, upStart+amount):
            if mat[k][i] != standard:
                res = "("+getArc(leftStart, upStart, amount//2) + getArc(leftStart+amount//2, upStart, amount//2) + \
                    getArc(leftStart, upStart+amount//2, amount//2) + \
                    getArc(leftStart+amount//2, upStart +
                           amount//2, amount//2)+")"
                return res

    return str(mat[upStart][leftStart])


print(getArc(0, 0, number))
