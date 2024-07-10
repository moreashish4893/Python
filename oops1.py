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



#2) the inheritance in which a class can be derived from another derived class is known as multilevel inhet...........  (A==>B(A)===>c(B))


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



## Hirarchical inheritance===(one parent have multiple child)

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


## Multiple inheritance :
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


