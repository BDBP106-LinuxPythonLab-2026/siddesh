
#
# qs10
# # def nextprime(n):
# #     import math
# #     if n < 2:
# #         return 2
# #     else:
# #         n = n + 1
# #         isprime = True
# #         while isprime == True:
# #             for i in range(2,int(math.sqrt(n)+1)):
# #                 if n % i == 0 :
# #                     isprime = False
# #                     break
# #
# #
# #
# #             if isprime == False:
# #                 n = n + 1
# #         if isprime == True:
# #             return n
#
# # n = int(input("enter the number"))
# # print(nextprime(n))








def nextPrime(n):
    if n < 2:
        return 2
    else:
      n = max(1, n) + 1
      while any(n % i == 0 for i in range(2, int(n**0.5) + 1)):
        n += 1
      return n


num = int(input("Enter an integer: "))
print(nextPrime(num))
