a=34
b=75

def mul():
    #existing
    global a,b
    a=43
    b=98
    print("Mul:",a*b)

mul()
print("Sum:",a+b)