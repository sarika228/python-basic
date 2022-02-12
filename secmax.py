a=[-5,40,-9,70,30,12,5,10,7]
i=0
max=0
s_m=0
while i<len(a):
    if a[i]>max:
        s_m=max
        max=a[i]
    elif a[i]>s_m:
        s_m=a[i]
    i=i+1
# print(max)
print(s_m)
# if s_m<a[i] and max>a[i]:
#     max=a[i]
# i=i+1
# print(s_m)