# # Program 2 - Product of All Digits
# Problem: A security system generates a verification value by multiplying all digits of a number.
# Example: 423 -> 4 x 2 x 3 = 24
# Another example: 5214 -> 40
# Accept a positive integer and display the product of all its digits.
# Think carefully about what value your product variable should contain initially.
def product(n):
    p=1
    while n>0:
        r=n%10
        p=p*r
        n=n//10
    return p    
n=int(input("Enter number:"))
print("product of all digits is",product(n)) 