# a={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
a=[1,2,3]
b=[5,6,7]
c=[9,10,11]
i=0
while i<len(a):
   j=0
   while j<len(b):
       k=0
    #    print("c1","c2","c3")
       while k<len(c):
            print(a[i],b[j],c[k])
            k=k+1
            j=j+1
            i=i+1

# for i in a.keys():
#     b=a[i]
#     j=0
#     while j<len(b):
#         c=[]
#         k=0
#         while k<len(b):
#             c.append(b[k][j])
#         k=k+1
#     print(c)
    #   table method
