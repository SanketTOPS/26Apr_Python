import re

#mystr="this is Python!"
mystr=input("Enter any string!:")

x=re.match("Python",mystr)
print(x)

if x: #true
    print("Match done...!")
else:
    print("Error!")