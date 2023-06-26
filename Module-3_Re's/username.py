import re

unm=input("Enter your username:")

x=re.findall('[A-Z]+[a-z]+[0-9]',unm)

if x: #true
    print("Username is valid!")
else:
    print("Invalid Username...")