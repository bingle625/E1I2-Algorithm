# 11721번

str = input()
res_str = ""
num = 0

for char in str:
    if(num < 10):
        num += 1
        res_str += char
    else:
        num = 1
        print(res_str)
        res_str = ""
        res_str += char

print(res_str)
