class person:
    def __init__(self,pid=0,na=""):
        self.id=pid
        self.name=na

    def take(self):
        self.id=int(input("Enter Person ID "))
        self.name=input("Enter Person Name ")

    def disp(self):
        print("ID= ",self.id)
        print("Name= ",self.name)

class teacher(person):
    def __init__(self,quli="",s=0):
        person. __init__(self)
        self.q=quli
        self.sal=s
    def enter (self):
        self.q=input("Enter Your Qualification ")
        self.sal=int(input("Enter Your Salary "))

    def show(self):
        print("Qualification= ",self.q)
        print("Salary= ",self.sal)

class subject(teacher):
    def __init__(self):
        teacher. __init__(self)
        self.sub=""
    def takesub(self):
        self.sub=input("Enter Your Subject ")
    def showtec(self):
        print("Subject= ",self.sub)

a=subject()
a.take()
a.enter()
a.takesub()
print()
print("----------------------------------------------Information--------------------------------------------")
a.disp()
a.show()
a.showtec()

input()        
