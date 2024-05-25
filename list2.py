a=['robert','ashish','mishrajii','more','abhishek','vishal']
b=[]
for i in a:
    if "r" in i:
        b+=[i]
        #b.append(i)
print(b)




# while loop
a=['robert','ashish','mishrajii','more','abhishek','vishal']
b=[]
i=0
while i<len(a):
    if 'r'in a[i]:
        b.append(a[i])
    i+=1
print(b)
