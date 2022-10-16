score = list(map(int,input()))

if sum(score[:len(score)//2]) == sum(score[len(score)//2:]):
    print("LUCKY")
else:
    print("READY")


