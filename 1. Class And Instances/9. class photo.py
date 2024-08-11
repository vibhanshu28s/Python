class photo:
    def __init__(self):
        self.pno=0
        self.category=""
        self.exhibit=""

    def fixexhibit(self):
        if (self.category=="Antique" or self.category=="antique"):
            self.exhibit="Zaveri"
        elif(self.category=="Modern" or self.category=="modern"):
            self.exhibit="Johnsen"
        elif(self.category=="Classic" or self.category=="classic"):
            self.exhibit="Terenida"
        else:
            self.exhibit="ERROR! This type of category is not found"

    def register (self):
        self.pno=int(input("Enter photo number "))
        self.category=input("Enter category ")
        self.fixexhibit()

    def disp(self):
        print("Photo Number= ",self.pno)
        print("Category= ",self.category)
        print("Exhibit= ",self.exhibit)

a=photo()
a.fixexhibit()
a.register()
print("---------------------------- Information ----------------------------")
a.disp()

input()
