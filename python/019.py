# Easy 2 - Email Checker
# Situation: A college wants to perform a basic check on the email address entered by a student.
# Your program should:
# • Ask the user to enter an email address.
# • Check whether it contains @.
# • Check whether it contains a dot (.).
# • Check whether it ends with .com.
# • If all conditions are satisfied, display 'Email looks valid'.
# • Otherwise display 'Invalid Email'.
# • Display the final email in lowercase.
user=str(input("Enter your email:"))
user=user.lower()
if "@" in user and "." in user and user.endswith(".com"):
    print("Email looks valid")
else:
    print("Invalid Email")
print(user)

#method 2
user = input("Enter your email:").lower()

has_at = "@" in user
has_dot = "." in user
has_com = user.endswith(".com")

if has_at and has_dot and has_com:
    print("Email looks valid")
else:
    print("Invalid Email")

print(user)