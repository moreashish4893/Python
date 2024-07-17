# #                                         OOPS   

# # Class is a blurprint that defines some properties and behaviors.An object is an instance of a class that has those properties and behaviors attached. A class is not allocated memory when it is defined .An object is allocated memory when it is created . Class is a logical entity whereas objects are physical entities. 



# # a=10
# # print roll_no(type(a))

# # b=20
# # print(type(a))

# # b="ashish"
# # print(type(c))

###################################################################################

# class student:
#     name="ashish"
#     email="a@gmail.com"
#     roll_no=444


#     def demo(self):                  #   self is a default parameter that represent instance of class
#         name="ashish"
#         print(name)
# s=student()
# s.demo()   

# k=student()
# k.demo()     

# m=student()
# m.demo()

###########################################################################################


# # class A:
# #     def demo(self,department):
# #         print(department)
# #         print(self)
# #         name="Ashish"
# #         age=28
# #         roll_no=444
# #         print(name,age,roll_no)


# #     def display(self):
# #         email="a@gmail.com"
# #         address="Kalyan"
# #         print(email,address)

# # a=A()
# # a.demo()
# # print(a)

# # a.display()
# # A.demo("k")
# # a.demo("Mech")


# ######################################################################################
 

# # class student:
# #     def show(self,name,roll_no):
# #         print("My name is",name)
# #         print("roll_no is",roll_no)
# #         print("I am a python developer")

# #     def display(self,name,roll_no):
# #         print("java developer")

# # s=student()
# # s.show("Ashish",444)
# # s.display("Abhi",222)

# #################################################################################################



# class student:
#     name="ashish"
#     email="a@gmail,com"

#     def show(self):
#         print(self.name,self.email)
#         print("python developer")

#     def display(self):
#         print(self.name)
#         print("java developer")

# a=student()
# #print(a.name)

# a.show()

# a.display()

# ######################################################################################################


#                                     Local Variable


# class A:
#     def show(self,roll_no,city):
#         print(roll_no,city)
#         name="Ashish"
#         age=28
#         print(name,age)

#     def display(self):
#         print(city)
#         email="a@gmail.com"
#         branch="IT"
#         print(name)
#         print(email,branch)

# a=A()
# a.show(444,"IT")
# print(a.name)
# a.display()

# ###################################################################################################
  
#                                  Instance Variable

# class A:
#     def show(self,name,age,salary):
#         a.name1=name
#         self.age1=age
#         self.salary1=salary
#         print(a.name1,self.age1,self.salary1)

#     def display(self):
#         print(a.name1,self.age1,self.salary1)

# a=A()
# a.show("Ashish",28,120000)      
# a.display()     



# #####################################################################################


# class A:
#     def show(self):
#         self.name="Ashish"
#         self.age=28
#         self.salary=90000

#     def display(self):
#         print(self.name)    
#         print(self.age)    
#         print(self.salary)    


# a=A()
# a.show()
# a.display()

# b=A()
# b.show()
# b.display()


# ##############################################################################################

# class A:
#     def show(self,name,address):

#         print("python developer")

#     def display(self):
#         self.show("ash","kalyan")
#         a.show("abhi","deloitte")

#         print("java")

# a=A()
# a.show("ash","thane")
# a.display()


# ###############################################################################################

# class A:
#     a=10
#     b=20  #21

#     def demo(s):
#         s.a=s.a+1      # 11
#         A.b=A.b+1      # 23

#         print(s.a,A.b)


# x=A()
# x.demo()

# y=A()
# y.demo()

# z=A()
# z.demo()

# ################################################################################################### 



#                                     Constructor


# # Constructor : __init__ method runs automatically when object is created which is used to initiliaze the instance object.

# class A:
#     def __init__(s):
#         print("Ashish")
#         s.id=10
#         s.name='Ashish'
#         s.salary=90000


#     def display(s):
#         print("id is",s.id)
#         print("name is",s.name)
#         print("salart is",s.salary)

# a=A()
# a.display()
# a.display()
# a.show()
# a.display()

# # ##############################################################################################################


# class A:
#     def __init__(s):
#         s.id=int(input("Enter id:"))
#         s.name=input("Enter name:")
#         s.salary=int(input("Enter salary:"))

#     def display(s):
#         print(f'id is{s.id} name is {s.name} and salary is{s.salary}')
#         print("name is",s.name)
#         print("salary is",s.salary)

# a=A()
# a.display()
# #a.display()
# a.show()
# a.display()


# x=A()
# x.display()


##############################################################################################################


# class A:
#     def __init__(s,name,age,salary):
#         s.name=name
#         s.age=age
#         s.salary=salary

#     def display(s):
#         print(s.name,s.age,s.salary)


#     def __str__(s):                           #  runs when object get printed
#         return s.name +" "+str(s.age)+" "+str(s.salary)

# a=A("Ashish",28,90000)
# a.display() 
# print(a)      

#####################################################################################################


# class A:
#     def display(s,name,age):
#         s.email='a@gmail.com'
#         print(name,age,s.email)
#         print("python developer")


#     def show(s):
#         print(s.email)
#         s.display("Ash",28)
#         print("java developer")


#     def demo(k):
#         print(k.email)    
#         print(a.email)    


# a=A()
# a.display("Abhi",25)
# a.show()
# #a.demo()


################################################################################################################

 #                                          Destructor

 # desctructor is a member method of a class...
 # it deletes the memory of object..
 # it can be call with object
 # name is : __del__
 #

 # Garbage Collector :
 # A program to delete reference
 # it runs automatically
 #it does memory management



# class A:
#     def __init__(self):
#         self.name="Ashish"
#         print("python dev")

#     def show(self):
#         print("java dev")

#     def __del__(self):
#         print("object deleted")

# a=A()
# a.show()
# #a.show()
# del a
#a.show()


#########################################################################################################################

      











                                           
























          






















             























