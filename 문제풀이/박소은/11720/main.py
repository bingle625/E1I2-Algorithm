
num = int(input())
line = input()
line_list = list(line)
sum = 0

for i in range(num):
    sum += int(line_list[i])

print(sum)
