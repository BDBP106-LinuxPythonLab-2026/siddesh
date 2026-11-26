



n = int(input("Enter a number: "))

width = len(str(n * n)) + 1

print(" " * width, end="")
for col in range(1, n + 1):
  print(str(col).rjust(width), end="")
print()

for row in range(1, n + 1):
  print(str(row).rjust(width), end="")
  for col in range(1, n + 1):
    print(str(row * col).rjust(width), end="")
  print()


# n = int(input("Enter a number: "))
#
# width = len(str(n * n)) + 1
#
# print(" " * width, end="")
# for col in range(1, n + 1):
#   print(f"{col:>{width}}", end="")
# print()
#
# # Print each row of the multiplication table
# for row in range(1, n + 1):
#   print(f"{row:>{width}}", end="")
#   for col in range(1, n + 1):
#     print(f"{row * col:>{width}}", end="")
#   print()
