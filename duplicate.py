a=[1,2,3,4,5,4,2]
b=[]
c1=[]
c=0
for i in a:
    if i not in b:
        b.append(i)
    else:
        c1.append(i)
print(b)
print(c1)
for i in b:
    c2=0
    for j in c1:
        if j==i:
            c2=c2+1

            if c2:
                print(f" {i} duplicates are {c2}")        

