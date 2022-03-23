n=int(input())
m=n
arm=0
while n!=0:
    p=n%10
    arm =arm + p
    n=n//10
print(arm)