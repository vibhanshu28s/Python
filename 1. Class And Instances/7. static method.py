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

@staticmethod
def FUN():
    print(abc.c)
