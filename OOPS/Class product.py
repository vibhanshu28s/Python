 # 5. Class Product
class product:
    def __init__ (self):
        self.pid=''
        self.pname=''
        self.pcostprice=0
        self.pmargin=0
        self.remark=''
        self.psellingprice=0
    def getdetail(self):
        self.pid=input('Enter product ID ')
        self.pname=input("Enter Product Name ")
        self.pcostprice=int(input("Enter Cost Price "))
        self.psellingprice=int(input("Enter Selling Price "))
        self.setremark()
    def setremark(self):
        self.pmargin=self.psellingprice-self.pcostprice
        if(self.pmargin>0):
            self.remark="Gain"
        else:
            self.remark="Loss"
    def disp(self):
        print("Product ID ",self.pid)
        print("Product Name ",self.pname)
        print("Cost Price ",self.pcostprice)
        print("Margin ",self.pmargin)
        print("Remark ",self.remark)
        print("Selling Price ",self.psellingprice)
a1=product()
a1.getdetail()
a1.setremark()
a1.disp()
        

        
