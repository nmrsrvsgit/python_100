# Program 1 - Factorial of a Number Problem: A company wants to calculate the number of possible arrangements of n different items using factorial. Example: 5! = 5 x 4 x 3 x 2 x 1 Ask the user for a positive integer and display its factorial. Example: Enter number: 5 -> Factorial = 120 Also decide what your program should do if the user enters 0 or a negative number.
def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1  
    return fact     
n=int(input("Enter n:"))
if n>0:
    print("Factiral of",n,"=",factorial(n))
elif n==0:
    print("Fatorial of 0 is 1") 
else:
    print("Please enter a positive number")
      