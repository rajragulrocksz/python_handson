a=0
b=1
n= int(input())
f=[a,b]
for i in range(2,n):
    c=a+b
    f.append(c)
    a=b
    b=c
print(f)
#Recursion

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fibn=[]
for i in range(n):
    fibn.append(fib(i))
print(fibn)