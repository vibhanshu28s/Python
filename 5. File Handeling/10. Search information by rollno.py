import pickle
class student:
    def __init__(self):
        self.n=''
        self.c=''
        self.r=''
        
    def take (self):
        self.n=input("Enter Student Name ")
        self.c=input("Enter Your Class ")
        self.r=input("Enter Roll Number ")
        
    def show(self):
        print('Rollno.= ',self.r)
        print('class= ',self.c)
        print('Name= ',self.n)

e=student()
f=open('v.txt','w')
for i in range (1,3):
    (e.take())
    pickle.dump(e,f)
f.close()

na=input('Enter Rollno= ')
c=0
f1=open('v.txt')
try:
    while True:
        e=pickle.load(f1)
        if(self.r==na):
            c=1
            e.show()
except EOFError:
    f1.close()
if c==0:
    print("No record Found")
