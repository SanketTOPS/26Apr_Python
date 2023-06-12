class studinfo:
    stid=12
    stnm='Sanket'

    def myfunc(self):
        print("This is class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)
        
    
# Object of class
st=studinfo()
print(st.stid)
print(st.stnm)
st.myfunc()
st.getsum(34,56)
