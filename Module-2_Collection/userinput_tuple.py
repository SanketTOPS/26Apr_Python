data=[]

n=int(input("Enter number of data:"))

for i in range(n):
    x=input("Enter your value:")
    data.append(x)

print(tuple(data))
