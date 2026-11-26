





grid = []
with open("stringmatrix.dat") as f:
    for line in f:
        if line.strip():
            grid.append(line.split())

n_rows = len(grid)
n_cols = len(grid[0])
print("Rows:", n_rows, "Columns:", n_cols)
print("grid =", grid)


columns = [[grid[i][j] for i in range(n_rows)] for j in range(n_cols)]
print("columns =", columns)


diagonals = []
for k in range(n_rows + n_cols - 1):
    diag = [grid[i][k - i] for i in range(n_rows) if 0 <= k - i < n_cols]
    diagonals.append(diag)
print("diagonals =", diagonals)
