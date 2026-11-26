special_chars = {"!", "@", "#", "$", "%", "&", "*"}

while True:
  password = input("Enter a password: ")


  has_upper = False
  has_lower = False
  has_digit = False
  has_special = False
  has_space = False


  for char in password:
    if char.isupper():
      has_upper = True
    elif char.islower():
      has_lower = True
    elif char.isdigit():
      has_digit = True
    elif char in special_chars:
      has_special = True
    elif char == " ":
      has_space = True


  errors = []

  if len(password) < 8:
    errors.append("- Must be at least 8 characters long.")
  if not has_upper:
    errors.append("- Must contain at least one uppercase letter.")
  if not has_lower:
    errors.append("- Must contain at least one lowercase letter.")
  if not has_digit:
    errors.append("- Must contain at least one digit.")
  if not has_special:
    errors.append(
        "- Must contain at least one special character (!, @, #, $, %, &, *)."
    )
  if has_space:
    errors.append("- Must not contain any spaces.")
  if "password" in password.lower():
    errors.append("- Must not contain the word 'password'.")

  # to check if any rules were broken
  if not errors:
    print("Password accepted!")
    break
  else:
    print("\nInvalid password. Please fix the following issues:")
    for error in errors:
      print(error)
    print()
