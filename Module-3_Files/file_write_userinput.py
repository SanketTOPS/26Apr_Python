fl=open('hello.txt','a')

def getdata():
    id=input("Enter ID:")
    name=input("Enter Name:")

    fl.write(f"ID={id}\nName={name}\n")

n=int(input("Enter number of students:"))
for i in range(n):
    getdata()

