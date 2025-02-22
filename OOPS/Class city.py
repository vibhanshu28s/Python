 # 13. Class city
class city:
    def __init__(self):
        self.code=0
        self.name=''
        self.pop=0
        self.km=0
        self.density=0
    def calDen(self):
        self.density=self.pop/self.km
    def Record(self):
        self.code=int(input("Enter City Code "))
        self.name=input("Enter City Name ")
        self.pop=int(input("Enter City Population "))
        self.km=int(input("Enter KM "))
        self.calDen()
    def disp(self):
        print("City Code= ",self.code)
        print("Name= ",self.name)
        print("Population= ",self.pop)
        print("KM= ",self.km)
        print("Density= ",self.density)
        if(self.density>12000):
            print("Highly Populated")

o=city()
o.Record()
print("------------------------")
o.disp()
