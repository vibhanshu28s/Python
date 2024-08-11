
f=open('w.txt','w')
l=[]
for i in range (1,6):
    a=input("Enter Name ")
    l.append(a)
print(l)
f.writelines(l)

f.close()

f1=open('w.txt','r')
l2=f1.read()
print(l2)
f1.close()

