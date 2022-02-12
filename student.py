student=[]
marks=[]
i=1
while i<=5:
    n=input("enter the student names:")
    student.append(n)
    j=1
    while j<=1:
        n1=int(input("enter the marks:"))
        marks.append(n1)
        j=j+1
    i=i+1
dictionary=dict(zip(student,marks))
print(dictionary)