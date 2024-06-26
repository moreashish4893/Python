# Types of argument

# 1)Positional argument
# 2)default argument
# 3)keyword argument
# 4)Variable length argument

#1)Ans:During a function call, values passed through argumnts should be in the order
# of parameters in the function definition.


##def simple_int(p,r,t):
##    print('principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple interst is:',si)
##
##p=5000
##r=10
##t=5
##simple_int(p,r,t)


#keyword argument:
##def simple_int(r,t,p):
##    print('principle is:',p) 
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple interst is:',si)
##
##simple_int(p=400,r=12,t=10)





#default argument

##def simple_int(p,r,t=10):
##    print('principle is:',p)
##    print('rate is:',r)
##    print('time is:',t)
##
##    si=p*r*t/100
##    print('simple interst is:',si)
##
##p=5000
##r=10
##t=5
##simple_int(p,r)





#scope
#local v:
##def display():
##    a=10
##    print(a)
##print(a)
##display(a)
##



#global v: A variable can be declared outside the function is called as global
#variable
#scope of variable is inside as well as outside the function.


##A=15
##def display():
##    a=10
##    b=20
##    print(a)
##    print(A)
##
##print(A)
##display()
##print(A)




##A=30
##def display():
##    A=20
##    print(A)
##print(A)
##display()
##print(A)



##A=30
##def display():
##    global A
##    A=20
##    print(A)
##print(A)
##display()
##print(A)
##


##
##B=30
##def display(x):
##    global a
##    a=a+x
##    return a
##a=20
##b=5
##display(b)
##print(a)     #25



##
##a=10
##y=5
##def myfun():
##    a=2
##    y=a
##    print(y,a)# 2,2
##myfun()
##print(y,a) #5,10







'''a=10
y=5
def myfun():
    #global a
    a=2
    y=a
    print(y,a) # 2,2
myfun()
print(y,a)#5,10'''
    




##a=10
##y=5
##def myfun():
##    global a
##    y=a
##    a=2
##    print(y,a) # 10,2
##myfun()
##print(y,a) #5,10



##a=10
##y=5
##def myfun():
##    a=2
##    y=a
##    print(y,a)#2,2
##
##myfun()
##print(y,a) # 5,10
##



'''a=10
y=5
def myfun():
    y=a
    a=2
    print(y,a)  #Error
myfun()
print(y,a) '''


###################################################################################################################






 















































