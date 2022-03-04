# 1181번

def sort2(str2):

    for i in range(53):
        res_set = set()
        for k in range(len(str2)):
            if len(str2[k]) == i:
                res_set.add(str2[k])

        res_list = list(res_set)
        res_list.sort()

        for t in range(len(res_list)):
            print(res_list[t])


num = int(input())

str = []

for i in range(num):
    str.append(input())

sort2(str)
