menu = {
    'Pizza' : 400,
    'Burguer':150,
    'Lacchi' :200,
    'Coffee' : 80, 
}

#Greet
print("Welcome to PYTHON Restaurant\n\n")
print("Here is our MENU:\n")
print("Pizza : Tk-400\nBurguer : TK-150\nLacchi : TK-200\nCoffee : TK-80\n")

Total_Order = 0
item_1 = input("Enter the name of the item you want to order : ")

if item_1 in menu:
    Total_Order += menu[item_1]
    print(f"{item_1} is added to in your order.")
else:
    print(f"{item_1} is not available ")

another_order = input("Do you want to order another item? (Yes/No)")
if another_order == 'Yes':
    item_2 = input("Enter the name of second item :")
    if item_2 in menu:
        Total_Order += menu[item_2]
        print(f"{item_2} is added to your order")
    else:
        print(f"{item_2} is not available !!")

    print(f"Your Total Bill : Tk-{Total_Order}")    
