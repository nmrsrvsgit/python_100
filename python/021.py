 # Medium 2 - Customer Feedback Analyzer
# Situation: A company wants to automatically inspect a customer's feedback message.
# Your program should:
# • Ask the user to enter a feedback message.
# • Convert it to lowercase for checking.
# • Check whether the word 'good' exists in the message.
# • Check whether the word 'late' exists in the message.
# • Count how many times the word 'service' appears.
# • Replace 'late' with 'delayed'.
# • Display the updated feedback message.
# Example: The service was good but delivery was late
feedback=input("Enter a feedback message:")
feedback=feedback.lower()
if "good" in feedback:
    print("Good exists")
if "late" in feedback:
    print("late exists")    
print(f"{feedback.count('service')} times service appeared.")
feedback=feedback.replace("late","delayed")
print("Updated feedback:",feedback)

