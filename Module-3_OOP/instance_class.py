class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

# calling via object
"""st=student()
st.getdata()
st.stid=34
st.stnm='Nirav'
st.getdata()"""

st=student()

# calling via instance
student().getdata()
student().stid=45
student().stnm='Ashok'
student().getdata()