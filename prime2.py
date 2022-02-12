i=1
while i<=100:
    j=2
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==1:
        print(i)
    i=i+1