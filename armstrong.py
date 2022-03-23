n=int(input())
m=n
arm=0
while n!=0:
    p=n%10
    arm =arm + pow(p,3)
    n=n//10
if arm==m:
    print("yes it is an armstrong number")
else:
    print(" Not an armstrong number")