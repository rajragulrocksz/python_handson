n=int(input())
m=str(n)
reverse=0
while n!=0:
    reverse=reverse*10 + n%10
    n=n//10
print("No",reverse)
r=''
print(m,r)
for i in range(1,len(m)+1) :
    r=r+m[-i]
    print(r)

print(r)