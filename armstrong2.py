n=1
ac=1
while n<=500:
    m=n
    j=len(str(m))
    sum=0
    while m>0:
        d=m%10
        m=m//10
        sum=sum+d**j
    if sum==n:
        print(n)
        ac=ac+1
    n=n+1


