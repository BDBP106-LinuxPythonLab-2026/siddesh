def swap_even_odd(lst):
    # Loop through even indices up to the second-to-last element
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


# Example list
data = [23, 32, 33, 44, "BDBH101", "hello", "python", 15, 1e-10, True, "hit"]

result = swap_even_odd(data)
print(result)
