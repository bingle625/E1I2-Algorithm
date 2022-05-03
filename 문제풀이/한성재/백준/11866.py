#11866 요세푸스 문제 0

N, K = map(int, input().split())

circle = [x for x in range(1,N+1)]
result = []

i = 0

while circle:
    i += K-1
    i = i % len(circle)
    result.append(str(circle.pop(i)))

resultString = ', '.join(result)

print("<{}>".format(resultString))
    