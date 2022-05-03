def complement(num: str):
    tmp = []
    for i in range(len(num)):
        if num[i] == '0':
            tmp.append('1')
        elif num[i] == '1':
            tmp.append('0')

    tmp = int("".join(tmp), 2)+1
    return tmp


def binary(num):
    tmp = bin(num)
    tmp = list(str(tmp))[2:]
    for i in range(32-len(tmp)):
        tmp.insert(0, '0')
    return tmp


def compare_bin(num1, num2):
    cnt = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            cnt += 1
    return cnt


num = int(input())
bin_num = binary(num)
comple_num = complement(bin_num)
comple_bin_num = binary(comple_num)
print(compare_bin(comple_bin_num, bin_num))
