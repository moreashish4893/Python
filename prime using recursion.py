def prime_no(n,i=2):
    if n < 2:                  # <---- base case
        return False
    if n % i==0:
        return False
    return prime_no(n,i+1)     

print(prime_no(5))    
    

