n=int(input("enter number: "))
count = 0
if n>0:
    while n>0:
        n= n//10
        count=count+1
    print("TOtaldigits = ",count)
else:
    print("please enter a positive number")         