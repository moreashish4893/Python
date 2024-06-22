def cal_sum(n):
    if(n==0):          # <---- base case
        return 0
    else:
        return cal_sum(n-1)+n
    
sum=cal_sum(5)
print(sum)
