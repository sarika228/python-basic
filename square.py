a=[{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},
{"name":"jaya","score":60,"school":"pyds"},{"name":"sonam","score":60,"school":"union"},
{"name":"Akshit","score":50,"school":"summer field school"}]
b={}
i=0
while i<len(a):   
    b[i]=a[i]  
    if a[i]["school"]=="pyds" and a[i]["score"]>=50:
        print(b[i])
    i=i+1

    


