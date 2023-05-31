import mylib

y="yes"

while y!="no":
    print("Choice 1: Add Data")
    print("Choice 2: Print Data")
    ch=int(input("Enter your choice:"))
    
    
    if ch==1:
        mylib.add_data()
    elif ch==2:
        mylib.prindata()
    y=input("Do you want to continue? : ")