i=1
a=[]
max=0
min=0
while i<=5:
    n=int(input("enter the number:"))
    a.append(n)
    if a[i]<min:
        min=a[i]
    print(min)
    if a[i]>max:
       max=a[i]
    print(max)
    i=i+1