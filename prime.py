num=int(input("enter a number:"))
i=1
while i<=num:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(i,"is a prime")
    i=i+1    
    