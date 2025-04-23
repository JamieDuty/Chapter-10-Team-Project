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

class CashRegister:
    def __init__(self):
        self.items = []
    def purchase_item(self, item):
        self.items.append(item)
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
    def get_cart(self):
        for item in self.items:
            print("Description:", item.get_description())
            print("Unit(s):", item.get_units())
            print("Price: $", item.get_price(), end = "")
    def empty():
        self.items = []
