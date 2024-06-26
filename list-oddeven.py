import random

random_list = [random.randint(1,100) for _ in range(10)]  # The _ placeholder indicating we dont need loop variable
Oddlist=[]
Evenlist=[]

for n in random_list :
    if n % 2 == 0:
        Evenlist.append(n)
    else:
        Oddlist.append(n)


print("Random List:", random_list)
print("Oddlist:",Oddlist)
print("Evenlist:",Evenlist)            