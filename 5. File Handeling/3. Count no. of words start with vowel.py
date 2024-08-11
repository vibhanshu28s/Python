f=open('vibhanshu.txt','r')
l=f.readline()
print(l)
c=0
for i in l:
    ch=i[0:1]
    if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u'):
        c=c+1
print(c)
