a=int(input())
sum=0
for i in range(1,(a//2)+ 1):
    if a % i==0:
        sum=sum+i
print("Prime_No : ", sum==1)
print("Perfect_No : ", sum==a)
