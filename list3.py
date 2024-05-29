a=[[['robert','ashish','anuj','abhishek']]]
'''for i in a[0][0]:
    #print(i)'''


for i in a:
    for b in i:
        for c in b:
            print(c) 




# while loop

'''a=[['robert','ashish','anuj','abhishek']]     

i=0
j=0
while i<len(a):
    while j <len(a[i]):
        print(a[i][j])
        j+=1
    
    i+=1'''


  


a=[[['robert','ashish','anuj','abhishek']]]     
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        k=0
        while k<len(a[i][j]):
            print(a[i][j][k])
            k+=1
        j+=1
    i+=1

