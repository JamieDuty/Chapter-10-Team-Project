#ACME_retail_system
#runs from chapter 10 team project.py
def main():
    #main will give the user the option to access the invetory system or retail system
    #it will then lead into the options in the inventory menu or the retail menu
    print("Please choose from the options below: ")
    print("To access the inventory control system, press 1.")
    print("To access the retail store, press 2.")
    print('')
    menu_choice = int(input("Enter your choice: "))
    #input handling here -------
    if menu_choice == 1:
        #run the inventory control menu


main()