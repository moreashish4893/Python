def simple_int(p,r,t):
    print('principle is:',p)
    print('rate is:',r)
    print('time is:',t)

    si=p*r*t/100
    print('simple interest is:',si)


p=5000
r=10
t=5

#######################################################################################################



def simple_interest(p,n,r):
    return(p*n*r)/100
values = []

for i in range(3):
    p=float(input(f"Enter Principle (p) for set {i+1}: "))
    n=float(input(f"Enter Number of years (n) for set {i+1}: "))         #     using loop
    r=float(input(f"Enter Rate of interest (r) for set {i+1}: "))

    interest = simple_interest(p,n,r)
    print(f"Simple interest for set {i+1}:{interest:.2f}")
