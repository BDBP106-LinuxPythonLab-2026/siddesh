def c_to_f(c):
    return c * 9 / 5 + 32

celsius = [0, 20, 37, 100]
print("in Fahrenheit ", list(map(c_to_f, celsius)))