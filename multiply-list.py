n = [2,3,4,5]

def multiply_list(n):
    result = 1
    for i in n:
        result = result * i
    return result

print("Multication of all numbers in the list:",multiply_list(n))




#########################################################################################


from functools import reduce

n=[2,3,4]                           
def multiply_list(n):
    return reduce(lambda x,y : x*y , n , 1)                          # using Higher Order Function

print("Multiplication of all numbers in the list:",multiply_list(n))