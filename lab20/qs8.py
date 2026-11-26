python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]

python_set = set(python_class)
java_set = set(java_class)

both_courses = python_set & java_set
print(f"Both courses ({len(both_courses)}): {both_courses}")

only_python = python_set - java_set
print(f"Only Python ({len(only_python)}): {only_python}")

only_java = java_set - python_set
print(f"Only Python ({len(only_java)}): {only_java}")

exactly_one = python_set ^ java_set
print(f"Exactly one course ({len(exactly_one)}): {exactly_one}")

all_students = sorted(python_set | java_set)
print(f"All unique students ({len(all_students)}): {all_students}")

name = input("\nEnter a student's name: ").strip()

if name in both_courses:
  print(f"{name} is enrolled in both Python and Java.")
elif name in python_set:
  print(f"{name} is enrolled only in Python.")
elif name in java_set:
    print(f"{name} is enrolled only in Java.")
elif name in java_set:
  print(f"{name} is enrolled only in Java.")
else:
  print(f"{name} is not enrolled in either course.")
