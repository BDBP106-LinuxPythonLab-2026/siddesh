#python


# # question 01
# # binary to decimal
# s = str(input("Enter your binary number: "))
# int_result = 0
# int_n = len(s)
#
#
# for i in range(int_n):
#     digit_val = int(s[i])
#     # print(int_digit_val)
#     int_result = (int_result * 2) + digit_val
#
#
# print(int_result)





# # qs 2
# # power rise to base
# import math
# b = int(input("Enter a number to base : "))
# p = int(input("Enter a number to exponent : "))
# print("(",b,p,")","=",math.pow(b,p))
# # print(math.pow(b,p))





# # qs 3
# # check for prime number
# import math
# p = int(input("Enter a number: "))
#
# is_prime = True
#
# for i in range(2, int(math.sqrt(p))+1):
#     if p % i == 0:
#         is_prime = False
#         print(p, "is not a prime number")
#         break
#
# if is_prime:
#             print(p,"is prime number")





# # qs 4
# # to  print individual digits of a given number
# N = str(input("Enter a number : "))
# for i in range(0, len(N)):
#     print(N[i])



# # qs 5
# # To print the first half of a string
# S = str(input("Enter a string/numbers..: "))
# for i in range(0, len(S)//2):
#     print(S[i],end=" ")



# # qs 6
# # print alternate characters
# s = str(input("Enter a string/number: "))
# n = 0
# while n in range(0,len(s)):
#     print(s[n],end=" ")
#     # n += 2
#     n = n+2






# # qs 7
# # to remove white space characters
# s = str(input("Enter a string: "))
#
#
# for c in s:
#     if c == " ":
#         del c
#
# print(s)
#




# # qs 8
# # to count the number of occurrence of words in the list
# s = str(input("Enter a sentence: "))
# word = str(input("Enter the word to count : "))
# def count_word(s):
#     count = 0
#     s.split(" ")
#     for i in s.split(" "):
#         if i in word:
#             count += 1
#     print(count)
#
# count_word(s)












# # question 10
#
# L = [10, 15, 22, 33, 40, 51, 68]
# even_numbers = []
#
# for num in L:
#   if num % 2 == 0:
#     even_numbers.append(num)
#
# print("Even numbers:", even_numbers)









# # question 12
# def subtract_matrices(m1, m2):
#   # using list comprehension
#   return [
#       [m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))
#   ]
#
#
#
# m1 = [[10, 20, 30], [40, 50, 60]]
#
# m2 = [[1, 2, 3], [4, 5, 6]]
#
#
# result = subtract_matrices(m1, m2)
#
#
# print("Result matrix (m1 - m2):")
# for row in result:
#   print(row)






# # question 13
#
#
# # initializing list
# test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
#
# # printing string
# print("The original list : " + str(test_list))
#
# # initializing K
# K = 2
#
# res = []
# for i in test_list:
#
#     # using count() to get count of elements
#     freq = test_list.count(i)
#
#     # checking if not already entered in results
#     if freq > K and i not in res:
#         res.append(i)
#
# # printing results
# print("The required elements : " + str(res))








# # qs 14
# # to remove all occurrences of an element from a list
# L = [34,376,5,2,4,3,3,3,3,3,3,3,3]
# L2 = L.copy()
# print(L.count(3))
# n = int(input("Enter a number to remove in L : "))
# count = 0
# for x in L:
#
#     print(L,L.index(x))
#     if n == x:
#
#         count += 1
#         L2.remove(x)
#         print(L)
# print("count",count)
# print(L2)



#
# L = [10, 20, 30, 20, 40, 20, 50]
# target = 20
#
# while target in L:
#     L.remove(target)
#
# print("Updated list:", L)
# # Output: Updated list: [10, 30, 40, 50]







# # question 15
# L = ["kite", "apple", "king", "banana", "key", ""]
# k = "k"
# result = []
#
# for word in L:
#     # Check 'if word' first to ensure the string is not empty
#     if word and word[0] == k:
#         result.append(word)
#
# print("Words starting with 'k':", result)
# # Output: Words starting with 'k': ['kite', 'king', 'key']
