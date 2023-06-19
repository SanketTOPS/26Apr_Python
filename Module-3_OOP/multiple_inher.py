class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class sanket:
    sid=0
    ssub=''

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.ssub=input("Enter Sanket's Subject:")

class tops(ashok,nirav,sanket):
    def printdata(self):
        print("-------Ashok's Data------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("-------Nirav's Data------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("-------Sanket's Data------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)

tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.s_getdata()
tp.printdata()