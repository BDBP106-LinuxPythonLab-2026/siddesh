students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]

total_score = 0

top_name, top_score = students[0]
bottom_name, bottom_score = students[0]

print("Student Grades:")
for name, score in students:
  if score >= 90:
    grade = "A"
  elif score >= 80:
    grade = "B"
  elif score >= 70:
    grade = "C"
  elif score >= 60:
    grade = "D"
  else:
    grade = "F"

  print(f"{name}: {score} ({grade})")

  total_score += score

  if score > top_score:
    top_score = score
    top_name = name

  if score < bottom_score:
    bottom_score = score
    bottom_name = name


class_average = total_score / len(students)

print(f"\nClass Average: {class_average:.2f}")
print(f"Top Scorer: {top_name} - {top_score}")
print(f"Bottom Scorer: {bottom_name} - {bottom_score}")
