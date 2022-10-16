#2000만 이하면 됨
#1204~

one = 0
zero = 0
number = input()
isOne = False
if number[0] == 1:
    isOne = True
    one += 1
else:
    zero += 1

for elem in number:
    if isOne:
        if elem == "0":
            zero += 1
            isOne = False
    else:
        if elem == "1":
            one += 1
            isOne = True
            
print(min(one,zero))