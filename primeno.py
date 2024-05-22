for n in range(2,101,1):
    for i in range(2,int(n**0.5)+1,1):
        if n % i==0:
        
            break
    else:
            print(n)
   

'''
   for n in range(1,101,1):
      for j in range(2,n,1):
         if n%j==0:
         break
      else:
      print(n) '''