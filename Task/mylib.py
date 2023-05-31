data=dict()
def add_data():
    keys=['name','price','qnt']
    for i in range(len(keys)):
        val=input(f"Enter your value for {keys[i]}:")
        data[keys[i]]=val
        

def prindata():
    print(data)

