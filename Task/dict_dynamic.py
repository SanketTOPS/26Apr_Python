mydict={}

keys=['id','name','sub','city']

#n=int(input("Enter number of pairs:"))

for i in range(len(keys)):
    value=input(f"Enter your value for {keys[i]}:")
    mydict[keys[i]]=value

print(mydict)