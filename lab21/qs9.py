


import math

def population_growth(initial, rate, time):
    def exponential_growth():
        return initial * math.exp(rate * time)

    print(" Population after time:", round(exponential_growth()))

population_growth(1000, 0.05, 10)
