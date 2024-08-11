class student:
    def __init__ (self):
        self.name=''
        self.roll=0
        self.p=0
        self.c=0
        self.m=0
        self.total=0
        self.per=0
        self.pf=''

    def take (self):
        self.name=input("Enter Your Name ")
        self.roll=int(input("Enter roll Number "))
        self.p=int(input("Enter marks in physics "))
        self.c=int(input("Enter marks in chemistry "))
        self.m=int(input("Enter marks in maths "))

    def cal(self):
        self.take()
        self.total=self.p+self.c+self.m
        self.per=(self.p+self.m+self.c)/3
        if (self.per<33.0):
            self.pf="Fail"
        else:
            self.pf=("Pass")

    def disp(self):
        print("Name = ",self.name)
        print("Roll Number = ",self.roll)
        print("Total = ",self.total,"/ 300")
        print(self.per,"%")
        print("Overall= ",self.pf)


ob1=student()
#ob1.take()
ob1.cal()
ob1.disp()



input()
                   
                   
                      
