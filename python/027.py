# Program 4 - Alternating Square Series
# # Problem: Ask the user for n and generate the series:
# 1, -4, 9, -16, 25, -36, 49, ...
# For n = 6, output: 1 -4 9 -16 25 -36
# Recognize two patterns at the same time:
# • how the numerical value changes
# • how the sign changes
def pattern(n):
    i = 1

    while i <= n:
        term = i * i

        if i % 2 == 0:
            term = -term
        else:
            term = term

        print(term, end=" ")
        i = i + 1


n = int(input("Enter number of terms: "))
pattern(n)