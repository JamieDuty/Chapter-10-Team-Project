#Chapter 10 Team Project
class RetailItem:      #Done by Jamie
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price
    #####-----getter methods-----#####
    #all should be strings
    def get_description(self):
        return self.__description
    def get_units(self):
        return self.__units
    def get_price(self): 
        return self.__price