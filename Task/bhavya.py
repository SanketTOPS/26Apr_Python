# Create a program for implementaion of students result. (Nested if)

s1=int(input("Enter a subjct1:"))
s2=int(input("Enter a subjct2:"))
s3=int(input("Enter a subjct3:"))
s4=int(input("Enter a subjct4:"))
s5=int(input("Enter a subjct5:"))

if s1>=40 and s2>=40 and s3>=40 and s3>=40 and s4>=40 and s5>=40:
    total=s1+s2+s3+s4+s5
    print("Total",total)

    pr=total/5
    print("pr:",pr)

    if pr>=70:
        print("Result First Class")
    elif pr>=60:
        print("Result second class")
    elif pr>=50:
        print("Result third Class")
    elif pr>=40:
        print("Result pass")

else:
 print("Fail")

