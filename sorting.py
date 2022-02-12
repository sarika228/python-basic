a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
values = sorted(a.values()) 
b= {}
for i in values:
    for k in a.keys():
        if a[k] == i:
            b[k] = a[k]
            break
print(b)

