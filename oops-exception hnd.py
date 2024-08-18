

# Exceptional handeling :  An exception is an event, which occurs during the execution of a program, that interrupt  the  normal flow of the program's instructions.

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
##except Exception as e:                 # exception :handled all types of errors(exceptions)
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
# ##    print('value error',v)




#try:
# ##    print('Thane')
# ##    #print(2/0)
# ##    print(int('demo'))
# ##    print('Dadar')
# ##   ######except ZeroDivisionError as e:
# ##    print(e)
# ####except ValueError as v:
# ##    print('value error',v)
# ##    ####except Exception as e:
# ##    print('exception handeled',e)
# ####except:
# ##    print('exception handeled')




#try:
# ##    print('Thane')
# ##    #print(2/0)
# ##    print(int('demo'))
# ##    print('Dadar')
# ##   except:
# ##    print('exception handeled')             # error // default axcept must be last




#except ZeroDivisionError as e:
# ##    print(e)####except ValueError as v:
# ##    print('value error',v)
# ##    except Exception as e:
# ##    print('exception handeled',e)





#try:
# ##    print('thane')
# ##    try:
# ##        print(9/0)
# ##    except Exception as e:
# ##        print(e)
# ##    print('Mumbai')
# ##    try:
# ##        print(abc)
# ##    except Exception as e:
# ##        print(e)####except:
# ##    print('outer exception handeled')




##k=[]##try:##    print(k[2])##    print('thane')##    try:##        print(9/0)##    except Exception as e:##        print(e)##    print('Mumbai')##    try:##        print(abc)##    except Exception as e:##        print(e)####except:##    print('outer exception handeled')






##k=[]##try:##    #print(k[2])##    print('thane')##    try:##        print(9/0)##    except Exception as e:##        print(e)##    print('Mumbai')##    try:##        print(abc)##    except Exception as e:##        print(e)####except:##    print('outer exception handeled')######else:##    print('it will execute only when exception is not occured')##





###k=[]##try:##    print(k[2])##    print('thane')##    try:##        print(9/0)##    except Exception as e:##        print(e)##    print('Mumbai')##    try:##        print(abc)##    except Exception as e:##        print(e)####except:##    print('outer exception handeled')######else:##    print('it will execute only when exception is not occured')####finally:##    print('it always be executed')##
##print('thane')##raise NameError()##print('Mumbai')





##print('thane')##try:##    raise NameError()##except:##    print('exception handeled')##print('Mumbai')##





#print('thane')##try:##    raise InvalidAgeError()##except:##    print('exception handeled')##print('Mumbai')##





#class InvalidAgeError(Exception):##    pass####print('thane')##try:##    raise InvalidAgeError()##except InvalidAgeError as e:##    print('exception handeled')##print('Mumbai')##





##class InvalidAgeError(Exception):
##    def __str__(self):
##        return 'Invalid Age Error detected'
##
##print('thane')
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print(e)
##print('Mumbai')
##





#class InvalidAgeError(Exception):
##    def __str__(self):
##        return 'Invalid Age Error detected'
##
##print('thane')
##try:
##    raise InvalidAgeError()
##except Exception as e:
##    print(e)
##print('Mumbai')
##





#class InvalidAgeError(Exception):
##    def __str__(self):
##        return 'Invalid age detecte  




#age=int(input('Enter Your name: '))
##if(age>=18):
##    print('You can vote')
##else:
##    try:
##        raise InvalidAgeError()
##    except Exception as e:
##        print(e)






#x=1
##while(x<11):
##    if(x==5):
##        continue
##    print(x)
##    x=x+1






# class A:
#     def __init__(self,name,age):
#         print('python developer')
#     def show(self):
#         print('Hii')

# class B(A):
#     def __init__(self,name,age):
#         super().__init__('raj',32)
#         print('java developer')

#     def display(self):
#         print('Hello')


# b=B('rajesh',31)







































































































