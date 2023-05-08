mobile=input("Enter your mobile number:")
print(mobile)

"""if mobile.isdigit():
    print("Valid mobile number")
else:
    print("Error!Invalid mobile number")"""



if len(mobile)<=10:
    if mobile.isdigit():
        print("Valid mobile")
else:
    print("Invalid mobile")