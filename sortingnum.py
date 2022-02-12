a={'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for i in a.keys():
    b=a[i]
    n=0
    while n<len(b):
        j=0
        while j<len(b)-1:
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
            j=j+1
        n=n+1
    a[i]=b
print(a)
    
    
    