def sort_num(blocks):
    for i in range(len(blocks)-1):
        if blocks[i] > blocks[i+1]:
            blocks[i], blocks[i+1] = blocks[i+1], blocks[i]
            for j in blocks:
                print(j, end=" ")
            print()
    if blocks != [1, 2, 3, 4, 5]:
        sort_num(blocks)


# map자료형은 len 함수 적용 안되므로 list로 형변환 필수
blocks = list(map(int, input().split()))
sort_num(blocks)
