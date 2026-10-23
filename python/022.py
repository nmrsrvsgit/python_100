# Hard 1 - Username & Password Registration Validator
# Situation: You are creating a simple registration system for a website. The user must enter a username and password, and
# the program should decide whether registration can continue.
# Your program should:
# Username rules:
# • Must not contain spaces.
# • Must contain at least 5 characters.
# • Must not start with an underscore (_).
# • Must not contain the word 'admin'.
# Password rules:
# • Must contain at least 8 characters.
# • Must contain at least one uppercase letter.
# • Must contain at least one lowercase letter.
# • Must contain at least one number.
# • Must contain at least one special character from @ # $ %.
# If both username and password satisfy all rules, display 'Registration Successful'. Otherwise, display suitable messages explaining what
# is wrong.
# Challenge: Do not solve everything using one giant condition. Break the problem into smaller checks
def check_username(username):
    errors=[]
    if " " in username:
        errors.append("username must not contain space")
    if len(username)<5:
        errors.append("username must contain atleast 5 characters")
    if username[0]=="_":
        errors.append("username must not start with underscore")
    if "admin" in username:
        errors.append("useranme must not contain word admin")
    return errors

def check_password(password):
    errors=[]
    if len(password)<8:
        errors.append("Password ,ust contain atleast 8 characters")
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    special_chars="@$%"    
    