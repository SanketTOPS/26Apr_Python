class student:
    def getdata(self,fname,lname):
        print("Fullname:",fname+lname)
    
    def getsum(self,a,b):
        print("Sum:",a+b)

st=student()
st.getdata('sanket','chauhan')
st.getsum(23,43)