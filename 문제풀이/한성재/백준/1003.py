#1003번 피보나치 함수

# import collections


# class sol(object):
#     dp = collections.defaultdict(int)
#     dp2 =collections.defaultdict(int)
    
#     def fiboOne(self,num):
#         if num == 0:
#             return 0
#         elif num == 1:
#             return 1
#         else:
#             self.dp[0] = 0
#             self.dp[1] = 1
#             for i in range(2, num+1):
#                 self.dp[i] = self.dp[i-1] + self.dp[i-2]                
#             return self.dp[num]

#     def fiboZero(self,num):
#         if num == 0:
#             return 1
#         elif num == 1:
#             return 0
#         else:
#             self.dp2[0] = 1
#             self.dp2[1] = 0
#             for i in range(2, num+1):
#                 self.dp2[i] = self.dp2[i-1] + self.dp2[i-2]
#             return self.dp2[num]

# number = int(input())

# for _ in range(number):
#     s = sol()
#     N = int(input())
#     print(s.fiboZero(N),s.fiboOne(N))
    
number = int(input())

fib_z = [-1] * 41
fib_o = [-1] * 41

fib_z[0] = 1
fib_z[1] = 0
fib_o[0] = 0
fib_o[1] = 1

for i in range(2, 41):
    fib_z[i] = fib_z[i-1] + fib_z[i-2]
    fib_o[i] = fib_o[i-1] + fib_o[i-2]

for _ in range(number):
    n = int(input())
    print(fib_z[n],fib_o[n])