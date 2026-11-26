




""" matops.py - simple vector and matrix operations for arbitrary sizes. """

def dot(a, b):

    """Dot product of two 3-D vectors; returns a number."""
    if len(a) != len(b):
        print("Error: vectors must have the same length for a dot product")
        return None
    return sum(x * y for x, y in zip(a, b))


def mat_vec(m, v):
    """Matrix-vector product; returns a vector."""
    if len(m) == 0 or len(m[0]) != len(v):
        print("Error: number of matrix columns must equal vector length")
        return None
    if any(len(row) != len(m[0]) for row in m):
        print("Error: matrix rows must all have the same length")
        return None
    return [dot(row, v) for row in m]


def mat_mat(a, b):
    """Matrix-matrix product; returns a matrix."""
    if len(a) == 0 or len(b) == 0 or len(a[0]) != len(b):
        print("Error: columns of first matrix must equal rows of second")
        return None
    if any(len(r) != len(a[0]) for r in a) or any(len(r) != len(b[0]) for r in b):
        print("Error: matrix rows must all have the same length")
        return None
    cols_b = list(zip(*b))
    return [[dot(row, col) for col in cols_b] for row in a]


def cross(a, b):
    """Cross product of two 3-D vectors; returns a vector."""
    if len(a) != 3 or len(b) != 3:
        print("Error: cross product needs two vectors of length 3")
        return None
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


if __name__ == "__main__":
    print(dot([1, 2, 3], [4, 5, 6]))                     # 32
    print(mat_vec([[1, 2], [3, 4], [5, 6]], [1, 1]))     # [3, 7, 11]
    print(mat_mat([[1, 2], [3, 4]], [[5, 6], [7, 8]]))   # [[19, 22], [43, 50]]
    print(mat_mat([[1, 2, 3]], [[1], [2], [3]]))         # [[14]]
    print(cross([1, 0, 0], [0, 1, 0]))                   # [0, 0, 1]
    print(dot([1, 2], [1, 2, 3]))                        # error -> None