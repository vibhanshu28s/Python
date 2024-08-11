class pen:
    def __init__(self,p=0):
        self.price=p
    def take(self):
        self.price=int(input("Enter price for pen "))
    def disp(self):
        print("Price= ",self.price)

class marker(pen):
    def __init__(self):
        pen.__init__(self)
    def show(self):
        print("Pen is used to write on paper")
        print("Marker is used to write on board")

class color(marker):
    def __init__(self):
        marker.__init__(self)
        self.col=" "
    def input(self):
        self.col=input("Enter Colour ")
    def dispshow(self):
        print("Colour =",self.col)

a=color()
a.take()
a.input()

print("------------------------------- INFORMATION -------------------------------")
a.disp()

a.show()

a.dispshow()

print(a.__dict__)
print(color.__name__)
print(color.__bases__)
print(a.__module__)
print(a.__doc__)

input()

