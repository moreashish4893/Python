def power(base,exponent):
    if(exponent==0):           # <---- base case     
        return 1
    else:
        return base * power(base,exponent-1)
    

print(power(2,3))
    