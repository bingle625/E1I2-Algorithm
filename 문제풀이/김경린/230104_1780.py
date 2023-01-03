from sys import stdin

size = int(stdin.readline())

all = [list(map(int, stdin.readline().rstrip().split())) for _ in range(size)]

def cut(num__minus_one, num_zero, num_one, paper):
    paper_size = len(paper)
    stand = paper[0][0]
    for i in range(paper_size):
        for j in range(paper_size):
            if paper[i][j] != stand:
                paper_size = paper_size // 3
                for k in range(3):
                    s = paper[paper_size*k:paper_size*(k+1)]
                    for l in range(3):
                        sliced = [ sliced_s[paper_size*l:paper_size*(l+1)] for sliced_s in s]
                        num__minus_one, num_zero, num_one = cut(num__minus_one, num_zero, num_one, sliced)
                return num__minus_one, num_zero, num_one
    
    if stand == -1:
        num__minus_one += 1
    elif stand == 0:
        num_zero += 1
    else:
        num_one += 1
    return num__minus_one, num_zero, num_one


num__minus_one, num_zero, num_one = cut(0,0,0,all)

print(num__minus_one)
print(num_zero)
print(num_one)

