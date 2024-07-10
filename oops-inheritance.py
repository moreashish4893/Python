#                                                Inheritance
#  
# one class can  derive the properties of another class this process is known as Inheritance

#class A:
##
##    a=10
##
##    def show(s):
##        print('python developer')
##
##class B(A):
##
##    b=20
##
##    def display(s):
##        print(s.b+B.b+x.b+s.a+A.a+x.a+B.a)
##        print('java developer')


##a=A()
##a.show()
##
##
##c=B()
##c.display()
##c.show()

#######################################################################################################


#                                              Types of inheritance
 
#1) single level inheritance

# Polymorphism
# Polymorphism means many form An entity can work in multiple role.this capability is called as polymorphism 
# 1) function overriding  
# 2) function overloading

# in function overriding we can declare a function in base class and derived class with same name and same parameter it occures when one class is inherit from another class(inheritance)


#class A:
##    def display(self):
##        print('python developer')
##
##class B(A):
##    def display(self):
##        print('java developer')
##
##
##ob=B()
##ob.display()


#more than one function with same name defined in same class and call with defferent parameter this process is known as method overloading..... but python does not support method overloading.


#class A:
##    def show(self):
##        print('Hiii')
##    def show(self,x):
##        print('bye')
##    def show(self,x,y):
##        print('hello')
##
##a=A()
###a.show()  #hello
###a.show(10)  #hi
##a.show(10,30) #bye

##
##class A:
##    def show(self,x,y):
##        print(x+y)
##
##a=A()
##a.show(10,30)
##
##
##
##class A:
##    def show(self,x=90,y=100):
##        print(x+y)
##
##a=A()
##a.show(10,30)


##
##class A:
##    def show(self,x=None,y=None):
##        print(x+y)
##
##a=A()
##a.show(10,30)
##
##
##
##class A:
##    def show(self,a=None,b=None,c=None):
##        if(a!=None and b!=None and c!=None):
##            print(a+b+c)
##        elif(a!=None and b!=None):
##            print(a+b)
##        else:
##            print(a)
##        
##            
##x=A()
##x.show(10)
##x.show(2,3)
##x.show(10,20,30)
##
##
##

##class A:
##    def show(self,a,b,c):
##        print(a+b+c)
##    def show(self,a,b):
##        print(a+b)
##    def show(self,a):
##        print(a)
##
##
##x=A()
##x.show(10,20,30)



# Exceptional handeling An exception is an event, which occurs during# the execution of a program, that interrupt  the    normal flow of the# program's instructions.

# the try block which is used to test a block of code for errors.
# the except block used to handle the errors.


 ##print('python developer')
 # ##a=int(input('Enter the first number: '))
 # ##b=int(input('Enter the second number: '))
 # ##try:
 # ##print(a/b)
 # ##except:
 # ##print('exception handeled')
 # ##print('java developer')



#print('Hiiii')
##a=[11,22,33,44,55]
##try:
##print(a[len(a)])
##except:
##print('list index out of range')
##print('Hello')




#print('Hiiii')
##a=[11,22,33,44,55]
##try:
##print(a[len(a)])
##except Exception as e:
##print(e)
##print('Hello')



#print('python developer')
##a=int(input('Enter the first number: '))
##b=int(input('Enter the second number: '))
##try:
##    print(a/b)
##except Exception as e:
##    print(e)
##print('java developer')


#print('python developer')
##
##
##try:
##    a=int(input('Enter the first number: '))
##    b=int(input('Enter the second number: '))
##    print(a/b)
##except Exception as e:
##    print('Value Error:',e)
##print('java developer')


#try:
    ##    print('Thane')
    # ##    print(2/0)
    # ##    print(int('demo'))
    # ##    print('Dadar')
    # ####except ZeroDivisionError as e:
    # ##    print(e)
    # ##    ##except Exception as e:
    # ##    print('exception handeled',e)


##try:
# ##    print('Thane')
# ##    print(2/0)
# ##    print(int('demo'))
# ##    print('Dadar')
# ##    ##except Exception as e:
# ##    print('exception handeled',e)
# ####except ZeroDivisionError as e:
# ##    print(e)    

##try:
# ##    print('Thane')
# ##    #print(2/0)
# ##    print(int('demo'))
# ##    print('Dadar')
# ##   ##except Exception as e:
# ##    print('exception handeled',e)
# ####except ZeroDivisionError as e:
# ##    print(e)####
# except ValueError as v:
# ##    print('value error',v)##    




