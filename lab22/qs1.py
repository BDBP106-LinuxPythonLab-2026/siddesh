


def greet_decorator(func):
    def wrapper():
        print("Hello! Calling the function...")
        func()
        print("After calling the function...")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator.")


message()
