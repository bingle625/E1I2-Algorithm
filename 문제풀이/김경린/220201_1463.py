
# dynamic programming

n = int(input())

# tryNum[i] -> i를 만드는데 드는 횟수? (*-//3,//2,-1을 해서 만드는)
tryNum = [0 for _ in range(n+1)]

for i in range(2, n+1):
    # i에서 -1을 하면 i-1이니까 횟수 +1을 기본으로
    tryNum[i] = tryNum[i-1]+1
    # //2 횟수와 -1을 한 횟수 비교
    if i % 2 == 0 and tryNum[i] > tryNum[i//2]+1:
        tryNum[i] = tryNum[i//2]+1
    # //3 횟수와 위에서 구한 최솟값 비교
    if i % 3 == 0 and tryNum[i] > tryNum[i//3]+1:
        tryNum[i] = tryNum[i//3]+1
print(tryNum[n])
