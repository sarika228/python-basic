n=int(input("enter the position:"))
i=1
count=0
while n>=0:
    j=1
    c=0
    while j<i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==1:
        if n==count:
            print(i)
            break
        count=count+1
    i=i+1