def triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a valid triangle"

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


a, b, c = 3, 4, 5
# triangle_area(a, b, c)
print(f"Sides: {a}, {b}, {c} -> Area: {triangle_area(a, b, c)}")
