result = [False for _ in range(30)]
for idx in range(28):
    result[int(input())-1] = True

for idx in range(30):
    if result[idx] == False:
        print(idx+1)