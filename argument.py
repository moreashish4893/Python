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
def simple_int(r,t,p):
    print('principle is:',p)
    print('rate is:',r)
    print('time is:',t)

    si=p*r*t/100
    print('simple interst is:',si)

simple_int(p=400,r=12,t=10)

