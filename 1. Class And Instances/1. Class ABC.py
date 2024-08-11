class ABC:
    def __init__ (self):
        self.i=0
        self.j=0
        self.k=0
    def take(self):
        self.i=int(input("Enter I Number "))
        self.j=int(input("Enter II Number "))
        self.cal()
    def cal(self):
        self.k=self.i+self.j
        self.disp()
    def disp(self):
        print("Sum= ",self.k)

x=ABC()
x.take()


