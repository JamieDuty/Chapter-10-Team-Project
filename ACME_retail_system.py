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
    menu_choice = int(input("Enter your choice: "))
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
        #run the retail menu
    
main()