import Chapter10TeamProject as file
import os
#INVENTORY VARIABLE IS LIST OF OBJECTS
#ACME_retail_system
#runs from chapter 10 team project.py
def main():
    while 1:
        if os.path.exists('inventory.txt'): #------> need to create the file somewhere else if it doesn't exist
            something = open("inventory.txt", "r")
            line = something.readline().rstrip()
            inventory = []
            while line != "":
                inventory.append(file.RetailItem(line, int(something.readline()), float(something.readline())))
                line = something.readline().rstrip()
        else:
            inventory = []
        #main will give the user the option to access the invetory system or retail system
        #it will then lead into the options in the inventory menu or the retail menu
        print("Please choose from the options below: ")
        print("To access the inventory control system, press 1.")
        print("To access the retail store, press 2.")
        print('')
        menu_choice = input("Enter your choice: ")
        while menu_choice.isdigit() == False:
            menu_choice = input('Enter 1 or 2 only: ')
        while menu_choice != '1' and menu_choice != '2':
            menu_choice = input("Enter 1 or 2 only: ")
            return menu_choice
        if menu_choice == '1':
            inventory_menu(inventory)
        if menu_choice == '2':
            cart = file.CashRegister()
            #run the retail menu
            #need handling??
            
            while 1:
                choice3 = retail_menu()
                if choice3 == "1":
                    display_cart(cart)
                if choice3 == "2":
                    display_items(inventory) 
                if choice3 == "3":
                    purchase_items(cart, inventory)
                if choice3 == "4":
                    start_over(cart)
                if choice3 == "5":
                    check_out(cart, inventory)
                if choice3 == "6":
                    break
        

def retail_menu():
    while 1:
        print("1 - View cart\n2 - Display items for sale\n3- Purchase item\n4 - Empty cart and start over\n5-Check out\n6 - Exit")
        choice2 = input("Please enter a selection: ")
        if choice2 in ["1", "2", "3", "4", "5", "6"]:
            return choice2

def display_cart(Cart):
    Cart.get_cart()

def display_items(inventory):
    display_inventory(inventory)

        
def inventory_menu(inventory):
    if os.path.exists('inventory.txt'): #------> need to create the file somewhere else if it doesn't exist
        print('Inventory file found, opening.')
        something = open("inventory.txt", "r")
        line = something.readline().rstrip()
        inventory = []
        while line != "":
            inventory.append(file.RetailItem(line, int(something.readline()), float(something.readline())))
            line = something.readline().rstrip()
            
    else:
        print('Inventory File does not exist, creating.')  
    password = 'Password'
    #run the inventory control menu
    #needs to search for inventory file, if not output creating
    user_password = input("Enter the inventory control password: ")
    while user_password != password:
        print('Incorrect!')
        user_password = input('Enter the inventory control password: ')
    print('Correct!')
    while 1:
        print('\nWelcome to the ACME inventory control system')
        print('\nPlease select an action from the following:')
        print('\nPress 1 to display the current inventory.')
        print('\nPress 2 to add inventory items to the current inventory.')
        print('\nPress 3 to save the inventory.')
        print('\nPress 4 to exit')
        inventory_choice = input('Select an action (1, 2, or 3. Press 4 to EXIT): ')
    
    #need handling
    
        if inventory_choice == '1':
            display_inventory(inventory)
        elif inventory_choice == '2':
            add_to_inventory(inventory)
        elif inventory_choice == '3':
            write_inventory_data(inventory)
        elif inventory_choice == '4':
            end()
            break
            
#Inventory Choices
def display_inventory(inventory):
    #display inventory needs to go into the inventory, read each line, and output it.
    #if there is nothing there, it needs to display that
    if len(inventory) != 0:
        print("Here is the current status of your inventory: ")
        for item in inventory:
            print("Description:", item.get_description())
            print("Unit(s):", item.get_units())
            print("Price: $", item.get_price(), sep = "")
    else:
        print("Here is the current status of your inventory: ")

def add_to_inventory(inventory):
    #add to inventory needs to add a description, number of units, and the price for the object TO THE LIST
    #it then needs to ask if you want to add another one
    #needs to take input, handle, and add to a list
    #take the inputs
    while 1:
        item = input("Enter an item description: ")
        item_units = input(f"Enter the number of units for {item}: ")
        while item_units.isdigit() == False:
            item_units = input(f'Enter the number of units for {item}: ')
        item_price = input(f"Enter the price per unit for {item}: ")
        while 1:
            try:
                item_price = float(item_price)
                break
            except:
                item_price = input(f'Enter the price per unit for {item}, (xx.xx format): ')

        new_inventory_item = file.RetailItem(item, item_units, item_price)
        inventory.append(new_inventory_item)
        go_again = input("Enter another item? (y/n): ")
        if go_again != 'y':
            break
    
def write_inventory_data(inventory):
    #write inventory data will update inventory.dat txt file with whatever is in the dictionary
    #it will then prompt the user to go into inventory or retail system
    #needs to take the list and upload to a file
        #check if file exists, if not create it
        #upload the data
        #output message
        #call og main
    inventory_file = open('inventory.txt','w')
    for item in inventory:
        inventory_file.write(item.get_description() + "\n")
        inventory_file.write(str(item.get_units()) + "\n")
        inventory_file.write(str(item.get_price()) + "\n")
    print('All data written.')
    print('\n---------------------------------------------------------------------')
    inventory_file.close()
  
#Retail Choices
    
def purchase_items(cart, inventory):
    while 1:
        while 1:
            display_inventory(inventory)
            item = input("What do you want to buy (n to exit): ")
            a = True
            if item.lower() == "n":
                a = False
                break
            for items in inventory:
                if items.get_description().lower() == item.lower():
                    cart.purchase_item(items.get_description(), items.get_price())
                    print(f"{item} has been added to your cart!")
                    break
        if not a:
            break
        while 1:
            choice9 = input("Do you want to buy something else(Y, N): ")
            if choice9.lower() in ("y", "n"):
                break
        if choice9 == "n":
            break
    

def start_over(Cart):
    Cart.empty()
    print("Cart has been emptied.")
    
def check_out(Cart, inventory):
    display_cart(Cart)
    print(f"Your total is ${Cart.get_total()}")
    choice10 = input("Press Y to complete the transaction, anything else to empty the cart and return to the main menu: ")
    if choice10 == "Y":
        for item in Cart.items.keys():
            for obj in inventory:
                if obj.description == item:
                    obj.set_units(obj.get_units() - 1)
        write_inventory_data()

def end():
    #end will the program.
    print('\nClosing.....')
    print('\nThanks for using the ACME Retail System and PoS Retail System.')
    print('\n--------------------------------------------------------------')
    
main()