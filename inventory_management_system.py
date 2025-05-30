inventory = {"shirts":100,"tshirts":80,"hoodies":250,"shorts":165}

while True:
    print("-------------------Inventory Management System-------------------")
    print("1.Enter New Product")
    print("2.Update Product Quantity")
    print("3.Delete Product")
    print("4.Search For Prodcut")
    print("5.Display Inventory")
    print("6.Exit")  

    select = int(input("Enter your choice from above menu(1-6):"))

    if select==1:
        Product=input("Enter New Prodcut Name:")
        if Product in inventory:
            print(f"{Product} already exists")
        else:
            qty=int(input(f"Enter Quantity for{Product}"))
            inventory[Product]=qty
            print(f"\n{qty} {Product} added!")

    elif select==2:
        Product=input("Enter prodcut name to update: ")
        if Product in inventory:
            qty=int(input("Enter new quantity number:"))
            inventory[Product]=qty
            print("\nQuantity updated!")
    elif select==3:
        Product=input("Enter the product name you want to delete:")
        if Product in inventory:
            del inventory[Product]
            print(f"\n{Product} deleted!")
        else:
            print(f"\n{Product}not found")

    elif select==4:
        Product=input("Enter the product name you want to search:")
        if Product in inventory:
            print(f"\nProdcut_name:{Product} Quantity:{qty} found in System")
        else:
            print(f"\n{Product} not found")

    elif select==5:
        print("---------INVENTORY---------\n")
        print("Item","              ","Qty")
        for k,v in inventory.items():
            print(k,"----------->",v)
    
    elif select == 6:
        print("Exiting!")
        break
    else:
        print("Invalid number enter number from 1-6")