class studinfo:

    @staticmethod
    def getdata(id,name):
        print("ID:",id)
        print("Name:",name)
    
    @staticmethod
    def getsum(a,b):
        print("Sum:",a+b)

st=studinfo()
st.getdata(101,'Nirav')
st.getsum(12,45)