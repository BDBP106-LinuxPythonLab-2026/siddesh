# qs 1

n = int(input("Enter an integer: "))

if n == 0 :
    print("0")

else:

    if n > 0 :
        print("Given number is positive")
    else :
        print("Given number is negative")


    if n % 2 == 0:
        print("Your number : ",n," is even")
    else:
        print("Your number : ",n," is odd")

    # check for divisible by 3 and 5
    if n % 3 == 0 and n % 5 == 0 :
        print("FizzBuzz number!")