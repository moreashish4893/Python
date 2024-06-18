#a=['robert','ashish','mishrajii','saud','abhishek','vishal']

'''i=0
while i<len(a):
    j=0
    c=0
    while j<len(a[i]):
        if a[i][j] in "aeiou":
            c=c+1
        j+=1
    print(f"{a[i]} this name contains{c} vowels")
    i+=1'''


'''for name in a:
    if len(name)==6:
         print(name)



for i in a:
     c=0
     for j in i:
          if j in "aeiou":
               c=c+1
     print(f"{i} this name contains{c} vowels")'''

     



b="i am ashish more"
c=[]
d=list(b)
 
for j in d:
     if j not in "aeiou":
          c.append(j)
print(c)
          
          
          

 
