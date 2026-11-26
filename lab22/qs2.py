




def before_after(func):
    def wrapper():
        print("before function is starting")
        func()
        print("after the function has finished!")
    return wrapper

@before_after
def calculate():
    print("Calculating...")


calculate()