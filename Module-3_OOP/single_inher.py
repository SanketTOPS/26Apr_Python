class student: #super calss
    stid=0
    stnm=''

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")

class tops(student): #sub class
    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)


tp=tops()
tp.getdata()
tp.printdata()
