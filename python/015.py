def chech_prime(n):
    if n<=1:
        print("not prime")
    else:
        i=2
        not_prime=0
        while i<n:
            if n%i ==0:
                not_prime=1
                break    
            i=i+1
        if not_prime:
             print(f"{n} is not a prime number") 
        else:
             print(f"{n} is a prime number")     
chech_prime(7)                     