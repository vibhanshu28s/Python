class abc:
    def __init__ (self):
        self.i=0
        self.j=0
        self.k=0

    def take(self):
        self.i=int(input("Enter I Number "))
        self.j=int(input("Enter II Number "))

    def cal(self):
        self.k=self.i+self.j

    def disp (self):
        self.take()
        self.cal()
        print("Sum= ",self.k)
        



a1=abc()
a1.disp()


