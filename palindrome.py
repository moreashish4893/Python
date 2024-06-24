#n=input("Enter a string:")

'''n="abccba"
if n == n[::-1]:
    print(f"{n} is a palindrome")                 # slicing method
else:
    print(f"{n} is not a palindrome")'''



    #################################################################################

n=int(input('Enter a number:'))
def palindrome(n):
    n1=n
    rev=0

    while n>0:
        d = n % 10
        rev = rev*10 + d
        n = n//10

    if n1==rev:
        print(f"{n} is a palindrome")
    else:
        print(f"{n}is not a palindrome")

        
