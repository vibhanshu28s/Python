class add:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
    def take (self):
        self.a=int(input("Enter I value "))
        self.b=int(input("Enter II value "))

    def cal (self):
        self.c=self.a+self.b
    def show(self):
        print("Sum= ",self.c)

class mul:
    def __init__(self):
        self.i=0
        self.j=0
        self.k=0
    def enter (self):
        self.i=int(input("Enter I value "))
        self.j=int(input("Enter II value "))
    def calc(self):
        self.k=self.i*self.j
    def disp(self):
        print("multiplication= ",self.k)

class maths(mul,add):
    def __init__(self):
        mul. __init__(self)
        add. __init__(self)
        print("class maths object created")
a=maths()
a.take()
a.cal()
a.show()
a.enter()
a.calc()
a.disp()



        
