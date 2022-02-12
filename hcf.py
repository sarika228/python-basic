n1=int(input("enter a n1 number:"))
n2=int(input("enter a n2 number:"))
if n1>n2:
    s=n2
else:
    s=n1
i=1
while i<=s:
    if n1%i==0 and n2%i==0:
        hcf=i
    i=i+1
print(hcf)



n1=int(input('enter a number'))
n2=int(input('enter a number'))
if n1>n1:
    s=n1
else:
    s=n2
i=1
while i<=s:
    if n1%i==0 and n2%i==0:
      lcm=i
    i=i+1
print(lcm)