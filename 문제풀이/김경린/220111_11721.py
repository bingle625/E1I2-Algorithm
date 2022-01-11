# 10개씩 끊어 출력하기
# 68ms

def slicing(strs: str):
    if len(strs) > 10:
        print(strs[0:10])
        strs = strs[10:]
        return slicing(strs)
    else:
        print(strs[0:])


strs = input()
slicing(strs)
