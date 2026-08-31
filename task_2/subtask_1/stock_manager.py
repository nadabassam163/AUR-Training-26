def loadStock():
    stock={}
    try:
        with open ("stock.txt") as s:
            for line in s:
                first=line.strip()
                parts=line.split(",")
                name=parts[0]
                quantity=int(parts[1])
                stock[name.lower()]=quantity
    except FileNotFoundError:
        print("error your file stock isn't found")
    except (ValueError,OSError):
        print("error your file stock isn't found")
    return stock

def showStockContents(stock):
    for i , (name,quantity) in enumerate(stock.items(),1):
        print(f"{i}. {name} : {quantity}")

def addToStock(stock):
    showStockContents(stock)
    choice = input("enter the name or the id:")
    if (choice.isdigit()):
        choice=int(choice)
        if choice in range(1,len(stock)+1):
         name=list(stock.keys())[choice -1]
        else:
            print("invalid id")
            return
    else:
        name=choice.lower()
    amount = input("enter the quantity to add:")
    if (not amount.isdigit() or int(amount)<=0):
            print("enter a valid quantity")
            return
    amount = int(amount)
    if name in stock:
        stock[name]=stock[name]+amount
    else:
        stock[name]=amount


def removeFromStock(stock):
    showStockContents(stock)
    choice = input("enter the name or the id:")
    if (choice.isdigit()):
        choice=int(choice)
        if choice in range(1,len(stock)+1):
         name=list(stock.keys())[choice -1]
        else:
            print("invalid id")
            return
    else:
        name=choice.lower();
        if name not in stock:
            print("not found")
            return
    amount = input("enter the quantity to remove:")
    if (not amount.isdigit() or int(amount)<=0):
                print("enter a valid quantity")
                return
    amount = int(amount)
    if (amount>stock[name]):
            print("no sufficient amount to remove")
    else:
            stock[name]=stock[name]-amount

def save(stock):
    with open("stock.txt","w") as s:
        for name,quantity in stock.items():
            s.write(f"{name},{quantity}\n")           


def main():
    stock=loadStock()
    while True:
        print("enter 1 to add stock")
        print("enter 2 to remove stock")
        print("enter 3 to show stock’s contents")
        print("enter 4 to exit the program")
        choice=int(input("enter your choice:"))
        if (choice not in range(1,5)):
             print("invalid choice please try again")
        if (choice == 1):
            addToStock(stock)
        elif (choice == 2):
            removeFromStock(stock)
        elif (choice == 3):
            showStockContents(stock)
        elif(choice == 4):
            save(stock)
            print("exiting the program")
            break


main()