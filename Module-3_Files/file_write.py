#fl=open('test.txt','w')
fl=open('test.txt','a')

"""fl.write("Good Morning!")
fl.write("\nHello Python!")"""

id=input("Enter ID:")
name=input("Enter Name:")

"""fl.write(id)
fl.write(name)"""

fl.write(f"ID={id}\nName:{name}\n")