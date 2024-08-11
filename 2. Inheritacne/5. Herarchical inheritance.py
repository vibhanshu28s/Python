class val:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
    def take (self):
        self.a=int(input("Enter I Value "))
        self.b=int(input("Enter II value "))

class add(val):
    def __init__(self):
    val.__init__(self)
        self.c=self.a+self.b
    def disp(self):
        print("Add= ",self.c)

class mul(val):
    def __init__(self):
        val.__init__(Self)
        self.c=self.a*self.b
    def show(self):
        print(self.c)

a=add()
a.disp

b=mul()
b.show()
        
        
