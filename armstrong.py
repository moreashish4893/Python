n=8208
#n=int(input("Enter a number:"))  
n1=n
l=len(str(n))
s=0
while n!=0:
    r = n%10
    s = s+r**l
    n =n//10

if n1 ==s:
    print(f"{n1} is an Armstrong number")
else:
    print(f"{n1} is not an armstrong number")
    

  