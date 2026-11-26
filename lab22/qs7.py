



from functools import wraps

import time
import math

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper


def population_growth(initial, rate, time_, verbose=True):
    def exponential_growth():
        return initial * math.exp(rate * time_)



@measure_time
def growth_loop():
    for _ in range(1_000_000):
        population_growth(1000, 0.05, 10, verbose=False)


# population_growth(1000, 0.05, 10, verbose=False)
growth_loop()