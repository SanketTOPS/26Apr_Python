import re

email="sanket.chauhan@gmail.com"

email_pattern="^[a-z0-9_.]+[@]+[a-z]+[\.]+[a-z]{2,4}$"

x=re.findall(email_pattern,email)

if x:
    print("Valid Email!")
else:
    print("Error!Invalid Email!")