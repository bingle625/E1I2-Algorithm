alnum = input()

alpha = []
num = []

for elem in alnum:
    if elem in "0123456789":
        num.append(elem)
    else:
        alpha.append(elem)
        
alpha.sort()
num.sort()

print("".join(alpha+num)) 
