import Chapter10TeamProject as file
import os
#INVENTORY VARIABLE IS LIST OF OBJECTS
#ACME_retail_system
#runs from chapter 10 team project.py
def main():
    #main will give the user the option to access the invetory system or retail system
    #it will then lead into the options in the inventory menu or the retail menu
    print("Please choose from the options below: ")
    print("To access the inventory control system, press 1.")
    print("To access the retail store, press 2.")
    print('')
    menu_choice = input("Enter your choice: ")
    #input handling here -------
    while menu_choice != '1' and menu_choice != '2':
        menu_choice = input("Enter 1 or 2 only: ")
        return menu_choice
    if menu_choice == '1':
        inventory_menu()
    if menu_choice == '2':
        cart = file.CashRegister()
        #run the retail menu
        
        while 1:
            choice3 = retail_menu()
            if choie3 == "1":
                display_cart(cart)
            if choie3 == "2":
                display_items(inventory) 
            if choie3 == "3":
                purchase_items(cart, inventory)
            if choie3 == "4":
                start_over(cart)
            if choie3 == "5":
                check_out(cart, inventory)
            if choie3 == "6":
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
    display_inventory

        
def inventory_menu():
    if os.path.exists('inventorydat.txt'):
        print('Inventory file found, opening.')
    else:
        print('Inventory File does not exist, creating.')  
    password = 'Password'
    #run the inventory control menu
    #needs to search for inventory file, if not output creating
    user_password = input("Enter the inventory control password: ")
    while user_password != password:
        print('Incorrect!')
        user_password = input('Enter the inventory control password: ')
    if user_password == password:
        print('Correct!')
        print('\nWelcome to the ACME inventory control system')
        print('\nPlease select an action from the following:')
        print('\nPress 1 to display the current inventory.')
        print('\nPress 2 to add inventory items to the current inventory.')
        print('\nPress 3 to save the inventory.')
        print('\nPress 4 to exit')
        inventory_choice = input('Select an action (1, 2, or 3. Press 4 to EXIT): ')
        #needs handling
    while inventory_choice != 4:
        if inventory_choice == 1:
            display_inventory()
        elif inventory_choice == 2:
            display_inventory()
        elif inventory_choice == 3:
            display_inventory()
        elif inventory_choice == 4:
            end()  

            
#Inventory Choices
def display_inventory(inventory):
    #display inventory needs to go into the inventory, read each line, and output it.
    #if there is nothing there, it needs to display that
    if len(self.items) != 0:
        for item in self.items:
            print("Description:", item.get_description())
            print("Unit(s):", item.get_units())
            print("Price: $", item.get_price(), end = "")
         

def add_to_inventory():
    #add to inventory needs to add a description, number of units, and the price for the object TO THE LIST
    #it then needs to ask if you want to add another one
    pass
def write_inventory_data():
    #write inventory data will update inventory.dat txt file with whatever is in the dictionary
    #it will then prompt the user to go into inventory or retail system
    pass
def end():
    #end will the program.
    print('Thanks for using the ACME Retail System.')        
#Retail Choices
    
def purchase_items(cart, inventory):
    while 1:
        while 1:
            display_inventory()
            item = input("What do you want to buy: ")
            for items in inventory:
                if items.get_description().lower() == item.lower():
                    cart.purchase_item(items.get_description(), items.get_price())
                    print(f"{item} has been added to your cart!")
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
    display_cart()
    print(f"Your total is ${Cart.get_total()}")
    choice10 = input("Press Y to complete the transaction, anything else to empty the cart and return to the main menu: ")
    if choice10 == "Y":
        for item in Cart.items.keys():
            for obj in inventory:
                if obj.description == item:
                    obj.set_units(obj.get_units() - 1)
        write_inventory_data()
        
    
main()