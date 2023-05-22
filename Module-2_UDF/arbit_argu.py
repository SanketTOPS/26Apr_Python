def getdata(*data):
    print("ID:",data[0])
    print("Name:",data[1])
    print("Subject:",data[2])


#getdata(101,'Ashok','PHP')

stid=int(input("Enter your ID:"))
stnm=input("Enter your Name:")
stsub=input("Enter your Subject:")
stcity=input("Enter your City:")

getdata(stid,stnm,stsub,stcity)

