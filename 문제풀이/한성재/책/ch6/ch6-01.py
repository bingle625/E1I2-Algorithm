def IsPal(s) -> bool:

    res_str = []

    for char in s:
        if(char.lower() in "abcdefghijklmnopqrstuvwxyz1234567890"):
            res_str.append(char.lower())

    for i in range(len(res_str)//2):
        if(res_str[i] != res_str[-i-1]):
            return False

    return True


init = input()
print(IsPal(init))
