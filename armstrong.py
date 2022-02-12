num=int(input("enter the number:"))
n=len(str(num))
count=num
sum=0
while num>0:
    a=num%10
    num=num//10
    sum=sum+a**n
if sum==count:
    print("armstrong")
else:
    print("not armstrong")