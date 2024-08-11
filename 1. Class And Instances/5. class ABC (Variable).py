class abc:
    c=0
    def __init__ (self):
        self.i=0
        self.j=0
        self.k=0
        abc.c=abc.c+1
        
    def take(self):
        self.i=int(input("Enter I Number "))
        self.j=int(input("Enter II number "))
        self.cal()

    def cal(self):
        self.k=self.i+self.j

    def disp(self):
        print("Sum= ",self.k, "C= ",abc.c)

a1=abc()
a2=abc()
a1.take()
a1.disp()
a2.take()
a2.disp()
a3=abc()
a3.take()
a3.disp()
a1.disp()
