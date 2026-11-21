def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return "Not a valid triangle"


    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


# Test cases
print("Sides (5, 5, 5):", classify_triangle(5, 5, 5))
print("Sides (5, 5, 8):", classify_triangle(5, 5, 8))
print("Sides (3, 4, 5):", classify_triangle(3, 4, 5))
