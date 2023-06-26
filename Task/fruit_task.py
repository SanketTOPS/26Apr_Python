#add to fruit
class Fruit:
    def __init__(self, fruitName, fruitPrice, sellUnit, stock):
        self.fruitName = fruitName
        self.fruitPrice = fruitPrice
        self.sellUnit = sellUnit
        self.stock = stock

#collet all fruits
store = []

def addFruit():
    fruitName = input("enter fruit name : ")
    fruitPrice = input("enter fruit price : ")
    fruitsellUnit = input("enter fruit sellUnit : ")
    fruitStock = input("enter fruit stock : ")

    f1 = Fruit(fruitName,fruitPrice,fruitsellUnit,fruitStock)
    store.append(f1)
    print('total fruits -> ',len(store))


# #heding
print("welcome to my fruit store")
# loging
userChoice = 3
while userChoice != 0:

    print("1 in to admin login")
    print("2 in to customer login")
    print("0 in to exit")
    userChoice = int(input('enter choice your number :'))

    if userChoice == 1: 
        adminChoice = 'Y'
        while adminChoice != 'X':
            print("welcome admin")
            print("A --> add fruit")
            print("U --> update fruit")
            print("R --> remove fruit")
            print("X --> back to login menu")
            adminChoice = input("admin choice :")
            if adminChoice == 'A':
                addFruit()
                print("fruit added")
            elif adminChoice == 'U':
                print("fruit updated")
            elif adminChoice == 'R':
                print("fruit removed")
            elif adminChoice == 'X':
                print("logout")
            
            else:
                print("unvalid input")

    elif userChoice == 2:
        customerChoice = 'Y'
        while customerChoice != 'X':
            print('welcome customer')
            print("P --> fruit purchese")
            customerChoice = input("customer choice: ")

            if customerChoice == 'P':
                print("fruit purchese")
            elif customerChoice == 'X':
                    print("logout")
            else:
                print("unvalid input")
        

    elif userChoice == 0:
        print("Thanks for visiting")

    else:
        print("unvalid input")
