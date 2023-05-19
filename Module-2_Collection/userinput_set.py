#nmset=set()
nmset=[]

n=int(input("Enter number of student's:"))

for i in range(n):
    nm=input("Enter your name:")
    #nmset.add(nm)
    nmset.append(nm)

print(set(nmset))