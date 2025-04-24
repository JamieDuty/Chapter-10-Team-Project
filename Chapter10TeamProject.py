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
    def set_units(self, new_units):
        self.units = new_units

class CashRegister:
    def __init__(self):
        self.items = {}
    def purchase_item(self, item, price):
        self.items[item] = price
    def get_total(self):
        total = 0
        for item in self.items.keys():
            total += items[item]
        return total
    def get_cart(self):
        if len(self.items) != 0:
        for item in self.items.keys():
            print(item, " <--> ", items[item], sep = "")
        else:
            print("Your cart is empty.")
    def empty():
        self.items = {}
