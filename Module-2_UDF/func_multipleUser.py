n=int(input("Enter number of students : "))

def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

for i in range(n):
    stid=input("Enter your ID:")
    stnm=input("Enter your Name:")
    stsub=input("Enter your Subject:")
    getdata(stid,stnm,stsub)



