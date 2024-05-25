#creating list with constructor method

a = list((1,2,'abc','xyz'))
print(a)
print(type(a))
print(len(a))


b = ['xyz','abc',123,44,55]
print(b)
print(type(b))
print(len(b))



a=['robert','ashish','mishrajii','saud','abhishek','vishal']
for i in a :
    if[-1]=="i":
    
      print(i)


for i in a:
        if 'r'in i:
            print(i)


for i in a:
    for j in i:
        if j=='r':
            print(i)
            break



i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]=='r':
            print(a[i])
            break
        j+=1
    i+=1





