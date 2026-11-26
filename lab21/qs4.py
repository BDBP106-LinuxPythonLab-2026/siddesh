



def fibonacci(n):
    seq, a, b = [], 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

n = 10
fib = fibonacci(n)
print("Fibonacci: ", fib)
print("    only even : ", list(filter(lambda x: x % 2 == 0, fib)))
print("    Only odd : ", list(filter(lambda x: x % 2 != 0, fib)))