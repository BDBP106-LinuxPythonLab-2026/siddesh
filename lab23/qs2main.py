from utils import math_utils , string_utils 

a, b = 34, 45
print("Add:", math_utils.add(a, b))
print("Subtract:", math_utils.subtract(a, b))
print("Multiply:", math_utils.multiply(a, b))
print("Divide:", math_utils.divide(a, b))
print("Remainder:", math_utils.remainder(a, b))

s1, s2 = "BDBH", "101"
print("Upper:", string_utils.to_upper(s1), string_utils.to_upper(s2))
print("Lower:", string_utils.to_lower(s1), string_utils.to_lower(s2))
print("Concatenate:", string_utils.concatenate(s1, s2))
