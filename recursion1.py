#recursion: when a function call itself,then that function is called as
### recursive function and the process is called as recursion
##
##
##def demo():
##    print('ashish')
##    demo()
##
##demo()
##
##i=0
##def demo():
##    glpbal i
##    i=i+1
##    print('ashish',i)
##    demo()
##
##demo()
##
##
##import sys
##
##print(sys.getrecursionlimit())
##
##sys.setrecursionlimit(200)   # to set recursion limit
##
##print(sys.getrecursionlimit())
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print('ashish',i)
##    demo()
##
##demo()
##


#Wap a program for fibbonacci series

##0,1,1,2,3,5,8,13,21,34,......
##
##
##fibo(1)=0
##fibo(2)=1
##fibo(3)=fibo(1)+fibo(2)
##fibo(3)=fibo(3-2)+fibo(3-1)
##fibo(n)=fibo(n-2)+fibo(n-1)



def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-2)+fibo(n-1)

n=int(input('Enter the number of terms: ')) #9
print(fibo(n))




 '''Questions : Print your name 10 times without using loop

 print factorial of number using recursion

 find the power of number using recursion

 find prime number using recursion

 wap of counting number of digit in given number

 sum of first nth number using recursion

 wap to printing  n to 1 sequence'''






























































































 


