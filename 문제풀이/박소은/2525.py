h, m = map(int, input().split())
t = int(input())

resultM = (m+t) % 60
resultH = h + (m+t)//60
resultH = resultH-24 if resultH>23 else resultH

print(resultH, resultM)