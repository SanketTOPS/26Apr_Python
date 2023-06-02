fl=open('hello.txt','r+')

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[2])

"""for i in fl:
    print(i)"""

fl.write("\nHello Python")

if fl.readable():
    print("Yes...")
else:
    print("Noo")
