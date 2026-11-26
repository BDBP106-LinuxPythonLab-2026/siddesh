

rows, cols = 3, 4
with open("stringmatrix.dat", "w") as f:
    for i in range(rows):
        letters = [chr(65 + i * cols + j) for j in range(cols)]
        f.write(" ".join(letters) + "\n")

