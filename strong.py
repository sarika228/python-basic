num=int(input("enter a num:"))
sum=0
temp=num
while num>0:
    i=1
    fac=1
    r=num%10
    while i<=r:
        fac=fac*i
        i=i+1
    sum=sum+fac
    num=num//10
if sum==temp:
    print(temp,"is a strong num")
else:
    print(temp,"is not a strong number")