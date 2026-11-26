


import math

def population_growth(initial, rate, time_, verbose=True):
    def exponential_growth():
        return initial * math.exp(rate * time_)

    result = round(exponential_growth())
    if verbose:
        print("Population after time:", result)
    return result


population_growth(1000, 0.05, 10)