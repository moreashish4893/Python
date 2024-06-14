#Variation  in user defined function

#function with no argument no return value

def add():
    a=10
    b=20
    print(f'addition of {a} and {b} is :' ,a+b)
add()





#function with argument no return value

def add(a,b):
    print(f'addition of {a} and {b} is :',a+b)
a=10
b=20
add(a,b)




#function with no argument but return value

def add():
    a=10
    b=20
    return a+b
    return f'addition of {a} and {b} is:',a+b
    print('hii') #after return no executable

sum=add()
print(sum)





#function with argument and return value

def add(a,b):

    return a+b
    return f'addition of {a} and{b} is:',a+b

sum=add(8,9)
print(sum)





def add(a,b):
    return a+b
    return f'addition of {a} and {b} is:',a+b
a=8
b=9
sum=add(a,b)
print(sum)


    
