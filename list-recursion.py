name=['ashish','shreyansh','vihan']

def print_list(list,idx=0):
    if(idx==len(list)):             # <---- base case
        return
    else:
    
        print(list[idx])
        print_list(list,idx+1)



print_list(name)        