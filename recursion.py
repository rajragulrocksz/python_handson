#Sum of Digits
def fact(n):
    if n==0 :
        return 0
    else:
        #print(res,n)
        return n % 10 + fact(n//10)
a=int(input())
print(fact(a))
re=0
#Reversal
def rev(n,re):
    if n==0:
        return re
    else:
        return  rev(n//10, n % 10 + re * 10)
print(rev(a,0))

#Armstrong
def arm(n,ar):
    if n==0:
        return ar
    else:
        ar = ar+ pow(n %10 ,3)
        return arm(n//10,ar)
print(arm(a,0)==a)