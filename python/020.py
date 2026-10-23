# Medium 1 - Mobile Number Privacy
# Situation: A website does not want to display a customer's complete mobile number on the screen.
# Your program should:
# • Ask the user to enter a mobile number.
# • Check that it contains exactly 10 characters.
# • Check that every character is numeric.
# • If valid, hide the first six digits and display only the last four digits.
# • Otherwise display 'Invalid Mobile Number'.
# Example: 9876543210 should become ******3210
mob_num=(input("Enter your mobile number:"))
if len(mob_num)==10 and mob_num.isdigit():
    print("******" + mob_num[-4:])
else:
    print("Invalid mobile number")    
