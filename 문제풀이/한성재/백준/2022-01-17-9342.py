# 9342번 염색체

# 마음에 안드는 답변
def detect_chro(chrosome: str) -> None:
    now_flag = 0
    good = "Good"
    infect = "Infected!"
    if(chrosome[0] in "ABCDEF"):
        if chrosome[0] == "A":
            now_flag += 1
        infection = ["A", "F", "C"]

        for i in range(1, len(chrosome)):

            if now_flag < 3 and chrosome[i] == infection[now_flag]:
                now_flag += 1
                continue

            elif chrosome[i] == infection[now_flag-1]:
                continue

            else:
                if i == len(chrosome)-1:
                    if chrosome[-1] in "ABCDEF":
                        return infect
                    else:
                        return good
                else:
                    return good

        if chrosome[-1] in "ABCDEF":
            return infect
        else:
            return good
    else:
        return good


num = int(input())


for _ in range(num):
    str = input()
    print(detect_chro(str))
