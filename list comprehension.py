odd=[i for i in range(1,101,2)]
print(odd)


even=[i for i in range(2,101,2)]
print(even) 


a=['robert','ashish','abhi']
print([i.upper() for i in a])

print([i for i in a if 'b' in i])




import random

names=['ashish','abhishek','vishal','saud','robert','anuj','rajith']

'''random_name=random.choice(names)
print(random_name)'''

print(random.choice(names))
    
print(random.choice(a))

print(random.choices(a,k=3))

print(random.sample(a,k=2))
  
random.shuffle(a)

print(a)

print(random.randint(1,10))
 
print("".join(random.sample('1234567890',k=4)))



