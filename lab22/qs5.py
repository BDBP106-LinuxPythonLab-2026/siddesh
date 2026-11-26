

from functools import wraps

import time

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

@measure_time
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("50! =", factorial(50))