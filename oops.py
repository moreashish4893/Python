#                                         OOPS   

# Class is a blurprint that defines some properties and behaviors.An object is an instance of a class that has those properties and behaviors attached. A class is not allocated memory when it is defined .An object is allocated memory when it is created . Class is a logical entity whereas objects are physical entities. 



# a=10
# print roll_no(type(a))

# b=20
# print(type(a))

# b="ashish"
# print(type(c))

###################################################################################

class student:
    name="ashish"
    email="a@gmail.com"
    roll_no=444


    def demo(self):   #self is a default parameter that represent instance of class
        name="ashish"
        print(name)

s=student()
s.demo()   

k=student()
k.demo()     

m=student()
m.demo()

##########################################################################################


# class A:
#     def demo(self,department):
#         print(department)
#         print(self)
#         name="Ashish"
#         age=28
#         roll_no=444
#         print(name,age,roll_no)


#     def display(self):
#         email="a@gmail.com"
#         address="Kalyan"
#         print(email,address)

# a=A()
# a.demo()
# print(a)

# a.display()
# A.demo("k")
# a.demo("Mech")


######################################################################################
 

# class student:
#     def show(self,name,roll_no):
#         print("My name is",name)
#         print("roll_no is",roll_no)
#         print("I am a python developer")

#     def display(self,name,roll_no):
#         print("java developer")

# s=student()
# s.show("Ashish",444)
# s.display("Abhi",222)

#################################################################################################



class student:
    name="ashish"
    email="a@gmail,com"

    def show(self):
        print(self.name,self.email)
        print("python developer")

    def display(self):
        print(self.name)
        print("java developer")

a=student()
#print(a.name)

a.show()

a.display()






