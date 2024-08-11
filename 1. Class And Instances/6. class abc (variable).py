class abc:
    c=0
    def __init__(self,x,y):
        self.i=x
        self.j=y
        self.k=0
        abc.c=abc.c+1

    def take (self,p,q):
        self.i=p
        self.j=q

    def cal(self):
        self.k=self.i+self.j

    def disp(self):
        print("Sum= ",self.k)

a1=abc(2,3)
a1=abc(4,5)
a1=abc(6,7)
a1=abc(8,9)
a1.take(10,20)
a1.disp()
        
