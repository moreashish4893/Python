a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
'''for i in a:
    for j in i:
        print(j)'''





        #while loop


i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1