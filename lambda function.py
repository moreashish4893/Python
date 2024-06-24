'''lambda function :  A function without a name is called as lambda function. 
It is also called anonymous function.
lambda function always starts with lambda keyword.


Syntax :

lambda arg_list : expression      <------syntax      

a = lambda x : print(x)
a(4)



a = lambda x : print(x**2)
a(4)



a = lambda x : x**2
print(a(4))



add = lambda x,y : print(x+y)
add(3,4)




def add(x,y):
    return x+y
print(add(3,4))



add = lambda x,y : (x+y,x-y)
print(add(3,4))




result = lambda x,y : (x+y,x-y)
print(result(3,4))



result = lambda x,y : (x+y,x-y)
add,sub =result(3,4)
print(add)
print(sub)



add = lambda x,y=5 : x+y
print(add(3)) 



add = lambda x=3,y=5 : x+y
print(add()) 



add = lambda y,x : x-y
print(add(x=3,y=9))'''


######################################################################################################################

'''A function which takes other function as argument is called as higher order function.

Types of higher order function :
1) filter()
2)map()
3)reduce()



True : True , non-zero
False : False , 0 , None



1) filter function :
This function is used to filter out element  of iterable.
filter function returns filter object'''

'''Syntax:
        filter(fun_name,iterable)

1)fun_name : function that test every element of iterable.
2)iterable : sequence which need to be filtered.'''


'''number=[11,22,33,44,66]

def even_fun(x):
    if x % 2==0:
        return True
    
filter_object = filter(even_fun,number) 
print(filter_object)

print(list(filter_object))
print(list(filter_object))'''


#################################################################################

'''number=[11,22,33,44,66]

def even_fun(x):
    if x % 2==0:
        return True
    
filter_object = list(filter(even_fun,number))
print(filter_object) 
print(filter_object) '''

##################################################################################

'''number=[2,3,7,9,11,18,15]

def prime(n):
    for i in range(2,n,1):
        if n%i==0:
           return False
    else:    
        return True
filter_object=list(filter(prime,number))
print(filter_object)    '''

  ##################################################################


 #2) Map function :map is also a higher order function ,it applies specific function on each element



'''n=[1,2,3,4,5,6]

def square(x):
    return x*x                          #  square
y=list(map(square,n))
print(y)'''

###################################################

a=[1,2,3,4,5,6]
def factorial(n):
    for i in range(1,n):
        n=n*i                                       # factorial
    return n
b=list(map(factorial,a))
print(b) 

####################################################################################


a=[1,3,5]
def fact(n):
    if(n==0 or n==1):                           # factorial
        return 1
    else:
        return n*fact(n-1)
b=list(map(fact,a))
    
print(b)

################################################################################

def fact(n):
    fact=1
    for i in range(1,n+1):                    # using for
        fact=fact*i
    print(fact)

fact(5)    

###############################################################################


n=4            
fact=1
i=1
while i<=n:                                  # using while
    fact=fact*i
    i+=1
print(fact)









         



