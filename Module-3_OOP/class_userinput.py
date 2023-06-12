class studinfo:
    stid=0
    stnm=""

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")

    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)


st=studinfo()
st.getdata()
st.printdata()