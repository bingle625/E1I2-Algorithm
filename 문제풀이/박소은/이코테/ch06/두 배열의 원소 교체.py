
N, K = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

print(sum(arrayB[0:K]) + sum(arrayA[K:]))