import Chapter10TeamProject as file
#ACME_retail_system
#runs from chapter 10 team project.py
def main():
    password = 'Password'
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
    if menu_choice == '1':
        #run the inventory control menu
        #needs to search for inventory file, if not output creating
        user_password = input("Enter the inventory control password: ")
        while user_password != password:
            print('Incorrect!')
            user_password = input('Enter the inventory control password: ')
        if user_password == password:
            print('Correct!')
            #go to inventory control system
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

def display_cart(cart):
    cart.get_cart()

def display_items(inventory):
    if len(self.items) != 0:
        for item in self.items:
            print("Description:", item.get_description())
            print("Unit(s):", item.get_units())
            print("Price: $", item.get_price(), end = "")
    
def purchase_items(cart, inventory):
    #resume
    cart.purchase_item(item)


def start_over(cart):
    cart.empty()
    
def check_out(cart, inventory):
    pass
main()