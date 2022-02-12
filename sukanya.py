a=input("enter the name:")
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    print(a[i],c)
    i=i+1
