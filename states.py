def line(a):
    f=open(a,'r')
    for line in f:
        s=line.split()
        if s[2]=="delhi":
            f=open("delhi.txt","a")
            f.write(s[0])
            f.write("\n")
        elif s[2]=="shimla":
            f=open("shimla.txt","a")
            f.write(s[0])
            f.write("\n")
        else:
            f=open("others.txt","a")
            f.write(s[0])
            f.write("\n")
    f.close()
line=("states.txt")