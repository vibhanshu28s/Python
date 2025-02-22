 # 10. Split Data

f=open('H:\\Python\\5. File Handeling\\vibhanshu.txt','r')
r=f.readlines()
for i in r:
    i=i.split()
print(i)
