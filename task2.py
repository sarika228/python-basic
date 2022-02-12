n=int(input("enter the number:"))
a=str(len(n))
sum=0
m=n
i=0
while i<=n:
    d=n%10
    n=n//10
    sum=sum+d**a
    i=i+1
if sum==n:
    print("number is armstrong")
else:
    print("the number is not armstrong")