#1259 팰린드롬수

inputNum = 1

while True:
    inputNum = input()
    
    if inputNum == "0":
        break
    else:
        isPal = True
        
        for i in range(len(inputNum)//2):
            if inputNum[i] != inputNum[-1-i]:
                isPal = False
                break
        if isPal:
            print("yes")
        else:
            print("no")