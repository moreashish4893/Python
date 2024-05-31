a= (1,2,3,'abc','xyz')
print(a)
print(type(a))
print(len(a))
print(a[-1])

#a[0]="Ashish"
#print(a)


b=(1,2)
print(type(a+b))
s=(1,)
print(type(s))


data=('ashish',28,'murbad',11,22,33,44,55)
(name,age,city,*a)=data
print(city)
print(a)


a=[1,2,3,([33,88,'abc',('yes','no','yes')])]
a[3][3]=('yes','yes','yes')
print(a) 


 
#another method

b=list(a[3][3])
b[1]='yes'
print(tuple(b))
a[3][3]=tuple(b)


      #

a=(1,2,3,3,5)
print(a[::-1])

print(a.count(2))
print(a.count(3))

print(a.index(3))

