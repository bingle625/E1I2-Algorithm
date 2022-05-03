# 덩치
def print_rank(member):
    for i in range(len(member)):
        rank = 1
        for j in range(len(member)):
            if i != j:
                if member[i][0] < member[j][0] and member[i][1] < member[j][1]:
                    rank += 1
        print(rank, end=" ")


num = int(input())
member = [[0 for _ in range(2)] for _ in range(num)]
for i in range(num):
    member[i][0], member[i][1] = map(int, input().split())

print_rank(member)
