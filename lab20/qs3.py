# qs 3 ( using binary tree search algorithm )
x = 44
count_attp = 0
for i in range(1,50):
     g = int(input("Guess a number between 1 and 50: "))
     count_attp += 1
     if g == x:
         print("you guessed right")
         print("number of attempts",count_attp)
         break
     elif g > x:
         print("your number is too high ")
         print("number of attempts",count_attp)

     elif g < x:
         print("your number is too low")
         print("number of attempts",count_attp)
     if count_attp == 7:
         print("the secret number is",x)
         break