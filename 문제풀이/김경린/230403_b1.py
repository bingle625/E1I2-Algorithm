# def toBinary(num, unit):
#     binary_num = ""
#     while num:
#         binary_num += str(num%2)
#         num //= 2
#     binary_num = binary_num[::-1]

#     left_zero = unit -len(binary_num)
#     binary_num = '0'*left_zero + binary_num
    
#     return binary_num


# n = int(input().rstrip())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

# for i in range(n):
#     arr1_binary = toBinary(arr1[i], n) 
#     arr2_binary = toBinary(arr2[i], n)
#     ans = ""
#     for j in range(n-1,-1,-1):
#         ans = ( '#' if int(arr1_binary[j]) or int(arr2_binary[j]) else " " ) + ans
#     print(ans)


        
n = int(input().rstrip())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


for i in range(n):
    ans = arr1[i] | arr2[i]
    print(bin(ans)[2:].zfill(n).replace('1', '#').replace('0', ' '))

