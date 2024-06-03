#print(ord('a'))
'''row=97
while row<=101:
    col=97
    while col<=row:
        print(chr(row),end=" ")
        col+=1
    row+=1
    print()'''





    

#reverse pattern
'''rows=5
while rows>0:
    print("*" * rows)
    rows -=1'''



#print(ord('e'))
row=101
col=5
while row>=97:
    print(chr(row)*col)
    row-=1
    col-=1
    print()



#print(ord('a'))
'''row=97
col=1
space=5
while row<=101:
    print(" "*(space-col)+chr(row))
row+=1
col+=1
print()'''
        
    









n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p+=1
    print()     




