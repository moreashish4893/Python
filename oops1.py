# Inheritance :
# one class can inherit the properties and method of another class this process is known as inheritence


##class A:
##    a=10
##    def show(s):
##        print('python developer')
##class B(A):
##   b=20
##    def display(s): 
##        print(s.b,s.a,B.b,B.a)
##        print('java developer')
##c=B()
##print(c.b)
##c.display()
##print(c.a)
##c.show()



# Types of inheritance:

# #1) single level inheritance
# #2) multilevel inhertance
# #3) hirarchical inheritance
# #4) Multiple inheritance
# #5) Hybrid inheritance



#2) the inheritance in which a class can be derived from another derived class is known as multilevel  inhetance...........  (A==>B(A)===>c(B))


##class A:
##    a=10
##    def show(s):
##        print('Grand parent method called')
##class B(A):
##    b=20
##    def display(s):
##        print('parent method called')
##class C(B):
##    c=30
##    def data(s):
##        print(s.a+s.b+s.c)
##        print('child method called')
##x=C()
##print(x.c)
##x.data()
##print(x.b)
##x.display()
##print(x.a)
##x.show()

#########################################################################################

## 3) Hirarchical inheritance===(one parent have multiple child)

## If multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance.

##class A:
##    a=10
# ##    def show(s):
# ##        print('python developer')
# ####class B(A):
# ##    b=20
# ##    def display(s):
# ##        print('java developer')
# ######class C(A):
# ##    c=30
# ##    def demo(s):
# ##        print()
# ##        print('django developer')
##b=B()
# ##b.display()
# ##b.show()
# ####x=C()
# ##x.demo()
# ##x.show()


###################################################################################################

##  4) Multiple inheritance :
##  if a child class inherits from more than one class, i.e. this child  class is derived from multiple classes, we call it multiple inheritance in Python.

##class A:
##    a=10
##    def show(s):
##        print('python developer')
##class B:
##    b=20
##    def display(s):
##        print('java developer')
##class C(A,B):
##    c=30
##    def demo(s):
##        print(s.c+s.b+s.a)
##        print()
##        print('django developer')
##x=C()
##x.demo()
##x.show()
##x.display()


##class Engineer:
##    def study(s):
##        print('Enginner study method called')
##    def show(s):
##        print('Enginner show method called')
# 
##class Doctor:
##    def study(s):
##        print('doctor study method called')
##    def display(s):
##        print('doctor display method called')
 
##class student(Engineer,Doctor):
##    def demo(s):
##        print('Pharmacist')
##s=student()
##s.display()
##s.show()
##s.study()


##class Engineer:    
## def study(s):        
## print('Enginner study method called')
##   def show(s):        
##print('Enginner show method called')

##class Doctor:    
## def study(s):        
## print('doctor study method called')
##   def display(s):        
## print('doctor display method called')

##class student(Doctor,Engineer):
##     def demo(s):        
## print('Pharmacist')

##s=student()
##s.display()
##s.show()
##s.study()

#################################################################################################


                                     # Polymorphism :

# An entity can work in multiple role. this capability is called as Polymorphism.
# 1)function overriding
# 2)function overloading
                          # 1)overriding

# in function overriding we can declare a function in base class  and derived class with same name and same parameter

# it occurs when one class is inherit from another class(inheritance)


# class A:
#     def display(self):
#         print("python developer")

# class B(A):
#     def display(self):
#         print("java developer")

# ob=B()
# ob.display()

####################################################################################################################

                         # 2) overloading
# more than one function with the same name defined in same class and call with different parameter
# but python does not support method overloading

# class A:
#     def show(self,x):
#         print("Hii")
#     def show(self,x,y):
#         print("bye")
#     def show(self):
#         print("Hello")

# a=A()
# a.show()      #hello  
# a.show(10)  #hi
# a.show(10,30)  #bye


# class A:
#     def show(self,x,y):
#         print(x+y)

# a=A()
# a.show(10,30)




# class A:
#     def show(self,x=90,y=100):
#         print(x+y)

# a=A()
# a.show(10,30) 



# class A:
#     def show(self,x=None,y=None):
#         print(x+y)

# a=A()
# a.show(10,30)

###################################################################################

# class A:
#     def show(self,a=None,b=None,c=None):
#         if(a!=None and b!=None and c!=None):
#             print(a+b+c)
#         elif(a!=None and b!=None):
#             print(a+b)
#         else:
#             print(a)

# x=A()
# x.show(10)
# x.show(2,3)            
# x.show(10,20,30)



###################################################################################################################

                                   #  Exceptional handeling 

# Exceptional handeling : An exception is an event, which occurs during  the execution of a program, that interrupt the normal flow of the program's instructions.


##print('python developer')##
# a=int(input('Enter the first number: '))
# ##b=int(input('Enter the second number: '))
# ##try:
# ##    print(a/b)
# ##except:
# ##    print('Exception handled')
# ##print('java developer')
# ##

##print('python developer')
# ##a=[11,22,3,64,35]
# ####try:
# ##    print(a[len(a)])
# ##except:
# ##    print('list index out of range')
# ####print('java developer')
# ##

##print('python developer')
# ##a=[11,22,3,64,35]
# ####try:
# ##    print(a[len(a)])
# ##except Exception as e:
# ##    print(e)
# ####print('java developer')##

##print('python developer')
# ##try:
# ##    a=int(input('Enter the number: '))
# ##    b=int(input('Enter the number: '))
# ##    print(a/b)##except Exception as e:
# ##    print(e)
# ##print('Hello')
# ##
##k=[]
# ##try:
# ##    print('thane')##    
# #print(9/0)
# ##    #print(abc)
# ##    #print(k[2])
# ##    print(int('rajesh'))
# ######except ZeroDivisionError as e:
# ##    print('zero division',e)
# ####except NameError as e:
# ##    print(e)
# ##except IndexError as e:
# ##    print(e)
# ##except ValueError as e:
# ##    print(e)
# ####except Exception as e:
# ##    print(e)
# ####except:
# ##    print('Exception handeled')   # default except block must be last####    

##try:
# ##    print('thane')
# ##    try:
# ##        print(9/0)
# ##    except Exception as e:
# ##        print(e)
# ##    print('mumbai')
# ##    try:
# ##        print(int('rajesh'))
# ##    except:
# ##        print('value Error')
# ##except:
# ##    print('Exception handeled outer try')##    

#k=[]
# ##try:
# ##    print(k[2])
# ##    try:
# ##        print(9/0)
# ##    except Exception as e:
# ##        print(e)
# ##    print('mumbai')
# ##    try:
# ##        print(int('rajesh'))
# ##    except:
# ##        print('value Error')
# ##except:
# ##    print('Exception handeled outer try')##
#      

##k=[11,22,33]
# ##try:
# ##    print(k[1])
# ##    try:
# ##        print(9/0)
# ##    except Exception as e:
# ##        print(e)
# ##    print('mumbai')
# ##    try:
# ##        print(int('rajesh'))
# ##    except:
# ##        print('value Error')
# ##except:
# ##    print('Exception handeled outer try')
# ##    ##else:
# ##    print('when exception is not occured')##


##k=[]
# ##try:
# ##    print(k[1])
# ##    try:
# ##        print(9/0)
# ##    except Exception as e:
# ##        print(e)
# ##    print('mumbai')
# ##    try:
# ##        print(int('rajesh'))
# ##    except:
# ##        print('value Error')
# ##except:
# ##    print('Exception handeled outer try')
# ##    ##else:
# ##    print('when exception is not occured')
# ##finally:
# ##    print('it always be executed')##
##try:
# ##    #print(9/0)
# ##    #print(abc)
# ##    print(int('rajesh'))
# ####except (ZeroDivisionError,NameError,ValueError) as e:
# ##    print(e)
##print('Hi')
# ##raise NameError()
# ##print('Hello')
##print('Hi')
# ##try:
# ##    ##    raise NameError()
# ##except:
# ##    print('Exception handle')
# ##print('Hello')
####class InvalidAgeError(Exception):
# ##    pass##
# ##print('Hi')
# ##try:
# ##    raise InvalidAgeError()
# ##except:
# ##    print('Invalid age error handled')
# ##print('Hello')




