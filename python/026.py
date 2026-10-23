# Program 3 - Generate the Pattern
# Problem: Ask the user for the number of terms n and generate the series:
# 2, 6, 12, 20, 30, 42, ...
# For n = 5, output: 2 6 12 20 30
# Do not hard-code the numbers. First observe how every term is generated from its position.

def patterns(n):
    i = 1

    while i <= n:
        term = i * (i + 1)
        print(term, end=" ")
        i = i + 1


n = int(input("Enter number of terms: "))
patterns(n)