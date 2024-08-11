class add:
    def __init__(self):
        self.i=0
        self.j=0
        self.k=0
    def take(self):
        self.i=int(input("Enter I Value "))
        self.j=int(input("Enter II value "))
    def cal(self):
        self.k=self.i+self.k

    def show(self):
        print("Sum= ",self.k)

class mul(add):
    def __init__(self):
        add. __init__(self)
        self.a=0
        self.b=0
        self.c=0
   
    def give(self):
        self.a=int(input("Enter I Number "))
        self.b=int(input("Enter II value "))
    def calc(self):
        self.c=self.a*self.b
    def disp(self):
        print("Multiplication= ",self.c)
    

a=mul()
a.take()
a.cal()
a.show()
a.give()
a.calc()
a.disp()
        
