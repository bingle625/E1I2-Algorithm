def solution(new_id: str):
    temp = new_id
    temp = temp.lower()
    arr = []
    for char in temp:
        if char not in ("abcdefghijklmnopqrstuvwxyz1234567890-_."):
            arr.append(char)
            arr = set(arr)
            arr = list(arr)
    print(arr)
    for char in arr:
        temp = temp.replace(char, "")
        print(temp)

    temp2 = ""
    while temp2 != temp:
        temp2 = temp
        temp = temp.replace("..", ".")

    if temp[0] == ".":
        temp = temp[1:]
    if temp[-1] == ".":
        temp = temp[:-1]

    if len(temp) == 0:
        temp = "a"
    elif len(temp) >= 16:
        temp = temp[:15]
        if temp[-1] == ".":
            temp = temp[:-1]

    if len(temp) <= 2:
        temp = list(temp)
        while len(temp) < 3:
            temp.append(temp[-1])

    answer = ''.join(temp)
    return answer


s = solution("!@#asldknsadasdasdlknsa@!#@#!12312425")

print(s)
