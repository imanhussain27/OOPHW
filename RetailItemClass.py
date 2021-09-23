class RetailItem:

    def __init__(self, description, inventory, price):
        self.__item_description=description
        self.__units_inventory=inventory
        self.__item_price=price

    def get_description(self):
        return self.__item_description
    def get_inventory(self):
        return self.__units_inventory
    def get_price(self):
        return self.__item_price