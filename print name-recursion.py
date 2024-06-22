def print_name(name,c=0):
    if c < 10:               # <--- base case
        print(name)
        print_name(name,c+1)

print_name("ashish")        
