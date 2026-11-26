


def check_positive(func):
    def wrapper(number):
        if number > 0:
            return func(number)
        print("Number must be positive")
    return wrapper

@check_positive
def square(n):
    print("Square:", n * n)
    
square(5)
square(-3)
