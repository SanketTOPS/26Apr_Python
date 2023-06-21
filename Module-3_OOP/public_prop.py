class student:
    stid=12
    stnm='Ashok'

    def getdata(self):
        print("This is getdata!")

st=student()
st.getdata()
print("ID:",st.stid)
print("Name:",st.stnm)