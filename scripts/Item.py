class Item:
    def init (self, item_id, name, quantity, price, supplier_id):
        self.item_id = item_id            # Unique identifier for the item
        self.name = name                  # Name of the tool
        self.quantity = quantity          # Quantity in stock
        self.price = price                # Price of the tool
        self.supplier_id = supplier_id    # Supplier identifier

    def updatequantity(self, amount):   # Update quantity
        self.quantity += amount

    def updateprice(self, new_price):   # Update price
        self.price = new_price

    def str(self): # String representation and Return value
       
        return "Item[ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Supplier ID: {self.supplier_id}]"
    
    
