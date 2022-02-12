n=int(input("enter the number:"))
a=len(str(n))
sum=0
m=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d**a
if sum==n:
    print("number is armstrong")
else:
    print("the number is not armstrong")