a=[1,3,105,7,9,90]
b=[]
i=0
while i<len(a): 
    if a[i]>1:
        for j in range(2,a[i],1):
            if a[i]%j==0:
                break
        else:  
            b.append(a[i])
    i+=1
print(b)




